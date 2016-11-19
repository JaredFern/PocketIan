import re, pdb
from fnmatch import fnmatch

NEXT_QUARTER = "spring"

global question_list, question_list_parsed
question_list, question_list_parsed =[], []

question_list= [
    "What are the prerequisites for *?",    # Course
    "What do I need to take for *?",        # Course
    "What are the * requirements?",         # major, minor, theme, honors, masters
    "How do I declare *?",                  # major, HARD CODE

    "Is * offered * quarter?",              # course, quarter
    "Who teaches *?",                       # course
    "Who teaches * during * quarter?",      # course
    "Who teaches * next quarter?",          # course

    "What courses count for *?",            # breadth_category
    "Is * available * quarter?",
    "What classes does * teach?",
    "What classes count for *?",

    "Does * count for the project requirement?",
    "Does * count for the breadth requirement?",
    "How are *'s CTEC's?",
    "What courses are available * quarter?"

    # "What is * about?",
    # "What is * prerequisite for?"
    # What are classes between * and * on *
 ]

# Variables: course_name, program, breadth_category, quarter

def questionToPattern():
    question_list_parsed = []
    for each in question_list:
        question_list_parsed.append(re.split('[ ]', each))
    return question_list_parsed

def read_tokenize(chat):
    chat = re.sub(r'[^\w\s]','',chat) + "?"

    tokenized_chat  = re.split ("[ ]", chat)
    return tokenized_chat

def match_question(chat_text):
    print (chat_text)
    tokenized_chat          =  read_tokenize(chat_text)
    question_list_parsed    = questionToPattern()

    for curr_question_ind, question in enumerate(question_list_parsed):
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
                    new_arg.replace('next', NEXT_QUARTER)
                    print (type(new_arg))
                    query_args.append(new_arg)

                    new_arg = []
                    qword_ind += 2
                else:
                    qword_ind += 1

            print ("Query Arg", query_args)
            return (curr_question_ind, query_args)
    return ("Try another question:\n", question_list)

match_question("Is 348 offered next quarter?")
