import re
from fnmatch import fnmatch

global question_list, question_list_parsed
question_list, question_list_parsed =[], []

question_list= [
    "What are the prerequisites for *?",
    "What is * prerequisite for?",
    "What are the * requirements?",
    "How do I declare *?",
    "Is * offered * quarter?",
    "What is * about?",
    "What time is * next quarter?",
    "Who teaches * during * quarter?",
    "Is * available next quarter?",
    "What courses count for *?",
    "Is * available next quarter?"
 ]

# Variables: course_name, program, breadth_category, quarter

def questionToPattern():
    question_list_parsed = []
    for each in question_list:
        question_list_parsed.append(re.split('[ ?]', each))
    return question_list_parsed

def read_tokenize(chat):
    tokenized_chat = re.split ("[ ?]", chat)
    return tokenized_chat

def match_question(chat_text):
    tokenized_chat          =  read_tokenize(chat_text)
    question_list_parsed    = questionToPattern()
    curr_question_ind       = 0

    for question in question_list_parsed:
        query_args         = []
        new_arg            = []
        question_len       = len(question)
        tokens_len         = len(tokenized_chat)
        reading_arg        = False

        if (fnmatch(chat_text,question_list[curr_question_ind])):
            print ('question matches:', question_list[curr_question_ind])
            qword_ind = 0

            for word in range (0, tokens_len):
                if (question[qword_ind] == '*') and (tokenized_chat[word] != question[qword_ind + 1]):
                    new_arg += tokenized_chat[word]
                elif (question[qword_ind] == '*') and (tokenized_chat[word] == question[qword_ind + 1]):
                    new_arg = "".join(new_arg)
                    query_args.append(new_arg)
                    new_arg = []
                    qword_ind += 2
                else:
                    qword_ind += 1
            print ("Query Arg", query_args)
            return (curr_question_ind, query_args)
        curr_question_ind += 1
    print ("No Match")
    return ("Try another question:\n", question_list)

match_question("Who teaches EECS 394 during winter quarter?")
