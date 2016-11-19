import re

global question_list
question_list = []

question_list= [
    "What are the prerequisites for <course_name>?",
    "What is <course_name> prerequisite for?",
    "What are the <program> requirements?",
    "How do I declare <program>?",
    "Is <course_name> offered <quarter>?",
    "Is <course_name> offered <quarter>?",
    "What’s <course_name> about?",
    "What time is <course_name> next quarter?",
    "Who is teaching <course_name>?",
    "Is <course_name> available next quarter?",
    "What courses count for <breadth_category>?",
    "Is <course_name> available next quarter?"
 ]

# Variables: course_name, program, breadth_category

def questionToPattern():
    for each in QB:
        each = re.split('[ ?]',each)


def read_tokenize(chat):
    tokenized_chat = re.split ("[ ?]", chat)
    return tokenized_chat

def match_question(tokens):
# Question matches the chat input, if every word that isnt a query_args matches
    tokens_len = len(tokens)
    for question in QB:
        query_args = []
        matched = True

        if (tokens_len) != len(question)):
            continue

        for word in question:
            markers = [question[0], question[-1]]
            if (markers == ['<', '>']):
                query_args.append(word)
            else:
                if (word != tokens[qword_count]):
                    matched = False
                    break

        if matched == True:
            return queryDB(question, query_args)
    return ("Try another question:\n", question_list)

def  queryDB():
