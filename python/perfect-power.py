# What's a Perfect Power anyway? - 5 kyu
# A perfect power is a classification of positive integers:

# In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer. More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.

# Your task is to check wheter a given integer is a perfect power. If it is a perfect power, return a pair m and k with mk = n as a proof. Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.

import math


def isPP(n):
    if math.sqrt(n).is_integer():
        return [int(math.sqrt(n)), 2]
    for i in range(2,math.floor(math.sqrt(n))+1):
        for j in range(2,11):
            if i**j == n:
                return [i,j]
            elif i**j > n:
                break
    return None
    

n1 = 4
n2 = 9
n3 = 5
n4 = 243
# print(isPP(n1))
# print(isPP(n4))
