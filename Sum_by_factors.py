'''https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python'''

#from sympy import primefactors
from math import sqrt
def sum_for_list(lst):
    def primefactor(n):
        n = abs(n)
        list_fact = set()
        while n % 2 == 0:
            list_fact.add(2)
            n = n // 2
        for i in range(3,int(sqrt(n)+1),2):
            while n % i == 0:
                list_fact.add(i)
                n = n // i
        if n > 2:
            list_fact.add(n)
        return list_fact
    factors_n_nums = []
    facts = set()
    for num in lst:
        for fact in primefactor(num):
            factors_n_nums.append((fact, num))
            facts.add(fact)

    list_return = []
    for test in sorted(facts):

        temp_hold = []
        for tupe in factors_n_nums:
            # print(tupe)
            if tupe[0] == test:
                temp_hold.append(tupe[1])
        # print(temp_hold)
        if temp_hold != []:
            list_return.append([test,sum(temp_hold)])
    return list_return
a = [15, 21, 24, 30, 45]
# a = [12, 15]
# a = [-29804, -4209, -28265, -72769, -31744]
print(sum_for_list(a))

