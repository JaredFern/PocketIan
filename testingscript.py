from question_parser import match_question, question_list
from dictionaries import professors_dictionary, course_dictionary, program_dict
# tests q0-q8, doesn't check spacing and capitalization and spelling errors
query_list = []
q = []
# iterate through courses
for key in course_dictionary:
    q.append("What are the prerequisites for *?".replace("*", key)) #q0
    q.append("What do I need to take for *?".replace("*", key)) #q1
    q.append("Who teaches *?".replace('*', key))#q5
    for quarter in ["fall","winter","spring"]:
        tmp = "Is * offered ^ quarter?".replace('*',key)#q4
        tmp = tmp.replace('^',quarter)
        q.append(tmp)
for depth in ["Theory", "Interfaces", "Systems", "A.I.", "Software"]:  # q6
    q.append("What courses count for *?".replace("*", depth))
# iterate through programs
for key in program_dict:
    q.append("What are the * requirements?".replace("*", key)) #q2
# iterate through profs
for key in professors_dictionary:
    q.append("What classes does * teach?".replace('*',key)) #q8
q.append("How do I declare a major?") #q3
'''
for i in q:
    print(i)
'''
for query in q:
    print(query + "               " + match_question(query))