class Course:
    def __init__(self, number, title, enforced_prereq, recommended_prereq, quarters_offered, breadths_fulfilled,
                 professors):
        self.number = number  # int
        self.title = title  # string
        self.enforced_prereq = enforced_prereq  # list of Courses
        self.recommended_prereq = recommended_prereq  # list of Courses
        self.quarters_offered = quarters_offered  # list of 3 ints, 0 or 1, [fall, winter, spring]
        self.breadths_fulfilled = breadths_fulfilled  # list of 5 ints, 0 or 1, [theory, systems, interface, A.I.,
        # software]
        self.professors = professors  # list of strings
