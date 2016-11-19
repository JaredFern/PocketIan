from importdata import course_dictionary as raw_dict
from pprint import pprint


class Course:

    def __init__(self, number, title, prereqs, quarters_offered, breadths_fulfilled,
                 professors):
        self.number = number  # string
        self.title = title  # string
        self.prereqs = prereq  # string
        # list of 3 ints, 0 or 1, [fall, winter, spring]
        self.quarters_offered = quarters_offered
        # list of 5 ints, 0 or 1, [theory, systems, interface, A.I., software]
        self.breadths_fulfilled = breadths_fulfilled

        self.professors = professors  # list of Professor instances


class Professor:

    def __init__(self, courses, ctec_score):
        self.courses = courses  # list of Courses
        self.avg_ctec = ctec_score  # int


def combine_pre_reqs(raw_course_dict):
    # output is course dictionary with combined pre req field
    for course_id in raw_course_dict:  # courseID keys
        # the dictionary of properties
        course_info = raw_course_dict[course_id]
        three_strings = [course_info["Enforced Pre-Requisites"], course_info[
            "Recommended Pre-Requisites"], course_info["Unenforced Pre-Requisites"]]
        nonempty_strings = []
        for pre_req in three_strings:
            if pre_req != "":
                nonempty_strings.append(pre_req)
        pre_req_string = ", ".join(nonempty_strings)

        course_info["Pre-Requisities"] = pre_req_string


def convert_field_booleans(raw_course_dict):
    # output is offered field converted from "F" to 1
    do_not_change = ["Title", "Enforced Pre-Requisites", "Recommended Pre-Requisites",
                     "Unenforced Pre-Requisites", "Professor", "Pre-Requisities"]
    for course_id in raw_course_dict:  # courseID keys
        # the dictionary of properties
        course_info = raw_course_dict[course_id]
        for info in course_info:  # A.I., Winter Quarter etc.
            if info not in do_not_change:
                if course_info[info] != "":
                    course_info[info] = 1
                if course_info[info] == "":
                    course_info[info] = 0


def parse_quarters(raw_course_dict):
    # input is a dictionary with info about the course, output is a list of 3
    # ints, 0 or 1, [fall, winter, spring]
    for course_id in raw_course_dict:  # courseID keys
        # the dictionary of properties
        course_info = raw_course_dict[course_id]
        fall = course_info["Fall Quarter"]
        winter = course_info["Winter Quarter"]
        spring = course_info["Spring Quarter"]
        course_info["Quarters"] = [fall, winter, spring]


def parse_breadths(raw_course_dict):
    # input is a dictionary with info about the course, output is a list of 5
    # ints, 0 or 1, [theory, systems, interface, A.I., software]
    for course_id in raw_course_dict:  # courseID keys
        # the dictionary of properties
        course_info = raw_course_dict[course_id]
        theory = course_info["Theory"]
        systems = course_info["Systems"]
        interface = course_info["Interfaces"]
        arti = course_info["A.I."]
        software = course_info["Software Development"]
        course_info["Breadths"] = [theory, systems, interface, arti, software]


def delete_unwanted_fields(raw_course_dict):
    # deletes unnecessary fields
    unwanted_list = ['Recommended Pre-Requisites',
                     'Unenforced Pre-Requisites', 'Enforced Pre-Requisites', 'Theory', 'Systems', 'Interfaces', 'A.I.', 'Software Development', 'Fall Quarter', 'Winter Quarter', 'Spring Quarter']
    for key, value in raw_course_dict.iteritems():
        for field in unwanted_list:
            value.pop(field, None)

test_dict = {'212': {'A.I.': 0,
                     'Core': 1,
                     'Enforced Pre-Requisites': '(110 or 111) and Math 230',
                     'Fall Quarter': 1,
                     'Interfaces': 0,
                     'Pre-Requisities': '(110 or 111) and Math 230',
                     'Professor': 'Vijayaraghavan',
                     'Project': 0,
                     'Recommended Pre-Requisites': '',
                     'Software Development': 0,
                     'Spring Quarter': 1,
                     'Systems': 0,
                     'Theory': 0,
                     'Title': 'Mathematical Foundations of CS',
                     'Unenforced Pre-Requisites': '',
                     'Winter Quarter': 0}, }

parse_quarters(raw_dict)
parse_breadths(raw_dict)
delete_unwanted_fields(raw_dict)
pprint(raw_dict)
# letters_to_booleans(raw_dict)
# combine_pre_reqs(raw_dict)
# pprint(raw_dict)

course_dictionary = {}
