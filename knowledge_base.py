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
    for each in QB:
        if (each[0] == '<' and each[-1] == '>'):
            each =


def read_tokenize(chat):
    tokenized_chat = chat.split (" ")
    return tokenized_chat

def match_question(tokens):
    matched_ind = null
    for question in QB:
        question_matched = True
        word_count = len(word)
        for word in question:
            marker = question[0]
            
            if (marker != '<'):
                if (word = tokens)
        if (matched_ind != null)
