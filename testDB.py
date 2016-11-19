course_dict = {'371': {'A.I.': 1,
                       'Core': '',
                       'Enforced Pre-Requisites': '',
                       'Fall Quarter': '',
                       'Interfaces': '',
                       'Pre-Requisities': ', , EECS 348 or EECS 325, or equivalent experience with artificial intelligence.',
                       'Professor': 'Forbus',
                       'Project': 1,
                       'Recommended Pre-Requisites': '',
                       'Software Development': '',
                       'Spring Quarter': '',
                       'Systems': '',
                       'Theory': '',
                       'Title': 'Knowledge Representationand Reasoning',
                       'Unenforced Pre-Requisites': 'EECS 348 or EECS 325, or equivalent experience with artificial intelligence.',
                       'Winter Quarter': ''}}

unwanted_list = ['Recommended Pre-Requisites','Unenforced Pre-Requisites', 'Enforced Pre-Requisites']
for key, value in course_dict.items():
	for field in unwanted_list:
		value.pop(field,None)

print(course_dict)