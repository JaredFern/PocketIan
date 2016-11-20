import re, pdb
from fnmatch import fnmatch

NEXT_QUARTER = "spring"

global question_list, question_list_parsed
question_list, question_list_parsed =[], []

question_list= [
    "What are the prerequisites for *?",    # Course
    "What do I need to take for *?",        # Course
    "What are the * requirements?",         # major, minor, theme, honors, masters
    "How do I declare a * in EECS?",                  # major, HARD CODE

    "Is * offered * quarter?",              # course, quarter
    #Is eecs 349 offered winter quarter?
    "Who teaches *?",                       # course
    # who teaches eecs 349?
    #"Who teaches * during * quarter?",      # course
    #"Who teaches * next quarter?",          # course

    "What courses count for *?",            # breadth_category
    "Is * available * quarter?",
    "What classes does * teach?",

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
        question_list_parsed.append(re.split('[ ?]', each))
        each = re.sub(r'[^\w\s]','',each)
    return question_list_parsed

def read_tokenize(chat):
    chat = re.sub(r'[^\w\s]','',chat)
    tokenized_chat  = re.split ("[ ]", chat)
    return tokenized_chat

def join_lower (str1):
    str1 = "".join(str1)
    str1.lower()
    str1.replace('next', NEXT_QUARTER)
    str1.replace('eecs', "")
    return str1

def match_question(chat_text):
    print (chat_text)
    tokenized_chat          =  read_tokenize(chat_text)
    # tokenized question list, no punctuation
    question_list_parsed    =  questionToPattern()
    curr_question_ind  = 0


    for question in question_list_parsed:
        query_args, new_arg =[],[]
        question_len       = len(question)
        tokens_len         = len(tokenized_chat)

        if (fnmatch(chat_text,question_list[curr_question_ind])):
            print ('question matches:', question_list[curr_question_ind])
            qword_ind = 0
            for word_ind in range (0, tokens_len):
                curr_token  = tokenized_chat[word_ind]
                curr_qword  = question[qword_ind]
                # checks if we've reached end of chat_text
                length_exc  = (qword_ind + 2 >= question_len)
                if (length_exc):
                    next_qword = ''
                else:
                    next_qword = question[qword_ind+1]
                print (curr_qword, curr_token, length_exc)
                if (curr_qword == '*'):
                    if (length_exc == False and curr_token != next_qword):
                        new_arg += curr_token
                    elif (length_exc == False and curr_token == next_qword):
                        query_args.append(join_lower(new_arg))
                        new_arg = []
                        qword_ind += 2
                    elif (length_exc == True):
                        new_arg += curr_token
                        query_args.append(join_lower(new_arg))
                        
                else:
                    print ("not added", question[word_ind])
                    qword_ind += 1
            print (query_args)
            return (curr_question_ind, query_args)
        curr_question_ind += 1
    return ("Try another question:\n", question_list)

match_question("What are the prerequisites for 348?")
