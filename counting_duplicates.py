def duplicate_count(text):
    '''accepts string, returns number of characters excluding spaces that appear 2 or more times'''
    dict_of_count = {}
    to_check = text.lower()
    for i in to_check:
        if i == ' ':
            pass
        elif i not in dict_of_count:
            dict_of_count[i] = 1
        else:
            dict_of_count[i] += 1
    counter = 0
    for i in dict_of_count:
        if dict_of_count[i] >= 2:
            counter += 1
    return counter
print(duplicate_count("Indivisibilities"))