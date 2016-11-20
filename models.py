class Course:
    invalid_inp = "That's not a valid EECS course!"

    def __init__(self, number, title, enforced_prereq, recommended_prereq, quarters_offered, breadths_fulfilled,
                 professors):
        self.number = number  # int
        self.title = title  # string
        self.enforced_prereq = enforced_prereq  # list of Courses
        self.recommended_prereq = recommended_prereq  # list of Courses
        # list of 3 ints, 0 or 1, [fall, winter, spring]
        self.quarters_offered = quarters_offered
        # list of 5 ints, 0 or 1, [theory, systems, interface, A.I.,
        self.breadths_fulfilled = breadths_fulfilled
        # software]
        self.professors = professors  # list of Professor instances


class Professor:

    def __init__(self, courses, ctec_score):
        self.courses = courses  # list of Courses
        self.avg_ctec = ctec_score  # int


class Program:
    input_format = ['major', 'minor', 'masters', 'theme', 'ba', 'bs',
                    'bsms', 'ms', 'b.a.', 'b.s.', 'm.s', 'B.S./M.S.', 'BS/MS', 'honors']

    def __init__(self, prereqs, reqs, count):
        self.course_count = count
        self.prereqs = prereqs
        self.reqs = reqs

# class Quarter:
#     input_format = ['next', 'fall', 'winter', 'spring']
#     invalid_inp = "That's not a real quarter!"
#     def __init__ (self, name, quarter):
#         if (name == 'next'):
#             self.name = 'spring'
#         self.name            = name
#         self.courses_offered = courses
