from dictionaries import *


def queryDB(question_num, query_args):

    if (question_num == 0 or question_num == 1):
        if (query_args[0] in course_dictionary):
            prereqs = course_dictionary[query_args[0]]["Pre-Requisities"]
        else:
            return ("I don't think that's a valid EECS course.")
        return "The prerequisites for " + query_args[0] + ": " + prereqs

    elif (question_num == 2):
        if (query_args[0] in program_dict):
            reqs = program_dict[query_args[0]]
        else:
            return ("That's not a valid EECS program!")
        return "The requirements for " + query_args[0] + " are " + reqs

    elif (question_num == 3):
        if(query_args[0] == "major"):
            return "Try going to the office of Heather Bacon (Tech L269) andd fill out a major declaration form."
        else:
            return "Idk maybe Google it?"

    elif (question_num == 4):
        class_name = query_args[0]
        quarter = query_args[1]
        quarters = ["fall", "winter", "spring"]
        if quarter == quarters[0]:
            quarter_num = 0
        elif quarter == quarters[1] or quarter == "next":
            quarter = "winter"
            quarter_num = 1
        elif quarter == quarters[2]:
            quarter_num = 2
        if(class_name in course_dictionary):
            if course_dictionary[class_name]["Quarters"][quarter_num] == 1:
                return "Yes, " + class_name + " is offered in the " + quarter
            else:
                quarters_offered = []
                for i in range(3):
                    num = course_dictionary[class_name]["Quarters"][i]
                    if num == 1:
                        quarters_offered.append(quarters[i])
                if len(quarters_offered) == 0:
                    return "Sorry, " + class_name + " is not offered this year"
                if len(quarters_offered) == 1:
                    return "No, but " + class_name + " is offered in the " + quarters_offered[0]
                if len(quarters_offered) == 2:
                    return "No, but " + class_name + " is offered in the " + quarters_offered[0] + " and the " + quarters_offered[1]
        else:
            return ("I don't think that's a valid EECS course!")

    elif (question_num == 5):
        course_num = query_args[0]
        if(course_num in course_dictionary):
            prof = course_dictionary[course_num]["Professor"]
            return "Professor " + prof + " teaches that class."
        else:
            return "I don't think that's a valid EECS class."

    elif (question_num == 6):
        breadth_query = query_args[0].lower()
        if breadth_query == 'theory':
            breadth_index = 0
        elif breadth_query == 'systems':
            breadth_index = 1
        elif breadth_query == 'a.i.':
            breadth_index = 2
        elif breadth_query == 'interfaces':
            breadth_index = 3
        elif breadth_query == 'software':
            breadth_index = 4
        else:
            return "I don't understand what breadth requirement that is"

        breadth_match = []
        for each in course_dictionary:
            if course_dictionary[each]['Breadths'][breadth_index]:
                breadth_match.append(each)

        return_message = 'The following EECS classes fulfill the " + query_args[0] + " requirement\n\n'
        for each in breadth_match:
            return_message += each + ': ' + \
                course_dictionary[each]['Title'] + '\n'

        return return_message

    elif (question_num == 7):
        course = query_args[0]
        quarter = query_args[1].lower()

        if quarter == 'fall':
            quarter_index = 0
        elif quarter == 'winter':
            quarter_index = 1
        elif quarter == 'spring':
            quarter_index = 2
        else:
            'I don\'t know which quarter that is...'

        if course in course_dictionary.keys():
            if course_dictionary[course]['Quarters'][quarter_index]:
                return 'Yes! ' + course + ' is offered in ' + quarter
            else:
                return 'No, ' + course + ' is not offered in ' + quarter
        else:
            return 'I don\'t think that course is being offered right now.'

    elif (question_num == 8):
        professor_name = query_args[0]
        if professor_name in professors_dictionary:
            queried_prof = professors_dictionary[professor_name].classes

            return_message = professor_name + 'teaches '
            for course in queried_prof.classes:
                return_message += 'EECS ' + course + ', '
            return return_message[:-2]

        else:
            return 'I don\'t know who that professor is'

    elif (question_num == 9):
        course = query_args[0]
        if course in course_dictionary:
            if course_dictionary[course]['Project']:
                return 'Yes!'
            else:
                return 'No'
        else:
            return 'That course number doesn\'t match any offered EECS course'

    elif (question_num == 10):
        course = query_args[0]

        if course in course_dictionary:
            breadth_list = course_dictionary[course]['Breadths']
            if 1 in breadth_list:
                return_message = 'EECS ' + course + ' fulfills '
                if breadth_list[0]:
                    return_message += 'Theory, '
                if breadth_list[0]:
                    return_message += 'Systems, '
                if breadth_list[0]:
                    return_message += 'A.I., '
                if breadth_list[0]:
                    return_message += 'Interfaces, '
                if breadth_list[0]:
                    return_message += 'Software, '
                return return_message[:-2]
            else:
                return 'EECS ' + course + ' fulfills no breadth requirements'
        else:
            return 'That course number doesn\'t match any offered EECS course'

    elif (question_num == 11):  # How are *'s CTEC's?
        prof = query_args[0]
        if prof in professors_dictionary:
            score = professors_dictionary[prof].avg_ctec
            return "That professor is great, their average CTEC score is " + score
        else:
            return "I don't know who that professor is..."

    elif (question_num == 12):
        quarter = query_args[0].lower()

        if quarter == 'fall':
            quarter_index = 0
        elif quarter == 'winter':
            quarter_index = 1
        elif quarter == 'spring':
            quarter_index = 2
        else:
            return 'I don\'t know which quarter that is...'

        return_message = 'The following EECS classes are offered in the ' + \
            query_args[0] + '\n\n'
        for each in course_dictionary:
            course_quarters = course_dictionary[each]['Quarters']
            if course_quarters[quarter_index]:
                return_message += each + ': ' + \
                    course_dictionary[each]['Title'] + '\n'
        return return_message
