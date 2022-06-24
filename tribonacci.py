def tribonacci(signature, n):
    '''Generates "Tribonacci" sequence to the nth place, sum of last 3 digits is equal the next
    https://www.codewars.com/kata/556deca17c58da83c00002db/train/python'''
    for i in range(n-3):
        signature.append(sum(signature[-3:]))
    return signature[0:n]

seed = [1,1,1]
print(tribonacci(seed,10))