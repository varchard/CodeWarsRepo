'''https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python'''
def first_non_repeating_letter(string):
    test_str = string.lower()
    counts = {}
    for let in test_str:
        if let in counts:
            counts[let] +=1
        else:
            counts[let] = 1
    for let in string:
        if counts[let.lower()] == 1:
            return let
    return ''