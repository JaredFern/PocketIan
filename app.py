import os
import sys
import json
import re
from question_parser import *
import requests
from flask import Flask, request
from autocorrect import spell
# from question_parser import *
from importdata import course_dictionary

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]  # the facebook ID of the person sending you the message
                    recipient_id = messaging_event["recipient"][
                        "id"]  # the recipient's ID, which should be your page's facebook ID
                    message_text = messaging_event["message"]["text"]  # the message's text

                    # words = re.findall(r"[a-zA-Z]+|[^a-zA-Z]+", message_text) # split string into list of alphabetical
                    # corrected = ''                                            # and non alphabetical substrings
                    # for word in words:
                    #     if re.match(r"[a-zA-Z]+$", word):  # only spell check the alphabetical strings
                    #         word = spell(word)
                    #     corrected += word


                    response_text = process(message_text)
                    send_message(sender_id, response_text)

                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def send_message(recipient_id, message_text):
    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


def process(message):
    return match_question(message)
    # test = "try: "

    # if message == "What courses are available next quarter?":
    #     return 'none u fkn idiot'

    # elif test in message:
    #     course_number = message[5:]
    #     if course_number in course_dictionary.keys():
    #         return "The title of EECS " + course_number + " is " + course_dictionary[course_number]['Title']
    #     else:
    #         return "I don't have an EECS course with that number"

    # return 'i dont understand wut ur sayin m8'


if __name__ == '__main__':
    app.run(debug=True)
