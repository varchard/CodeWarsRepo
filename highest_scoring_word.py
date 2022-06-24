'''the code handles the problem at https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python,
 the first code is my submitted anwser, the second is the refactored version'''
# from string import ascii_lowercase
# def high(x):
#     letter_score = {}
#     number = 1
#     for letter in ascii_lowercase:
#         letter_score[letter] = number
#         number +=1
#     word_list = x.split()
#     high_score = 0
#     big_word = ''
#     for word in word_list:
#         score = 0
#         for letter in word:
#             score += letter_score[letter]
#         if score > high_score:
#             big_word = word
#             high_score=score
#     return big_word

# print(high('man i need a taxi up to ubud'))

from string import ascii_lowercase
def high(x):
    '''refactored to take advantage of list comprehensions and loops and if statements being able to be on one line to be as short as possible'''
    letter_score ={ascii_lowercase[num]:num+1 for num in range(26)}
    high_score, big_word = 0, ''
    for word in x.split():
        score = 0
        for letter in word: score += letter_score[letter]            
        if score > high_score: high_score, big_word = score, word
    return big_word

print(high('man i need a taxi up to ubud'))
        
        