'''https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python'''
def valid_parentheses(string):
    if string.count('(') == 0 and string.count(')') == 0:
        return True
    elif string.count('(') == string.count(')'):
        test_string = string
        while test_string.count('(') > 0:
#            print(test_string.index('('),test_string.index(')'))
#            print(test_string[::-1].index(')'),test_string[::-1].index('('))
            if test_string.index('(') > test_string.index(')') or test_string[::-1].index(')') > test_string[::-1].index('('):
                return False  
            open_parenthesis = test_string.index('(')
            close_parenthesis = test_string.index(')')
            print(open_parenthesis,close_parenthesis)
            if open_parenthesis > close_parenthesis:
                return False
            test_string = test_string[:open_parenthesis] + test_string[open_parenthesis+1:close_parenthesis]+ test_string[(close_parenthesis+1):]
#            print(test_string)
        return True
    else:
        return False

#valid_parentheses('hi(hi)()')

'''somebody suggested a simple solution, use a counter to count opens, subtract from counter for close, 
if counter ever goes below zero you have closed more than you opened return false, 
if counter at the end is zero there are even number of open and close parenthesis'''
def valid_parentheses2(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0 
print(valid_parentheses2('hi(hi)()'))