from importdata import course_dictionary

def queryDB(question_num, query_args):
    if (question_num == 0):
        if (len(query_args) != 1):
            for each in course_title:
                lookup (query_args, course_dictionary)
            return ("That's not a valid EECS course!")

        # "What are the prerequisites for *?",
    elif (question_num == 1):
        # "What is * prerequisite for?",

    elif (question_num == 2):
        # "How do I declare *?",

    elif (question_num == 3):
        # "What are the * requirements?",

    elif (question_num == 4):
        # "Is * offered * quarter?",

    elif (question_num == 5):
        # "What’s * about?",

    elif (question_num == 6):
        # "What time is * next quarter?",

    elif (question_num == 7):
        # "Who teaches * during * quarter?",

    elif (question_num == 8):
        # "Is * available next quarter?"

    elif (question_num == 9):
        # "What courses count for *?",

    elif (question_num == 10):
        # "What quarters are * offered?",

    elif (question_num == 11):
        # "What quarter is * offered?",

    elif (question_num == 12):
        # "What classes does * teach?",
