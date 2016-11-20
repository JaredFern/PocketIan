from dictionaries import professors_dictionary

l = ['Tumblin', 'asdf', 'asdfoisg sdoi fj']
for i in l:
    if i not in professors_dictionary.keys():
        print(i)