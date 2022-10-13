# Best Travel - 5 kyu

# John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

# Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?

# t = max sum of distances
# k = number of towns to visit
# ls = list of distances

import itertools
import re
from collections import Counter

def choose_best_sum(t, k, ls):
    # all permutations of k length sub-lists of distances
    # sum of each permutation
    # highest sum <= t
    filtered = sorted(filter(lambda x: x <= t, ls))
    if len(filtered) < k:
        return None
    combs = list(itertools.combinations(filtered, k))
    sums = [sum(x) for x in combs]
    sums = list(filter(lambda x: x<=t, sums))
    if len(sums) == 0:
        return None
    return max(sums)
    

ls1 = [50, 55, 56, 57, 58]
#choose_best_sum(163, 3, ls1) # -> 163


ls2 = [50]
#choose_best_sum(163, 3, ls2) # -> null

ls3 = [91, 74, 73, 85, 73, 81, 87] 
#choose_best_sum(230, 3, ls3)  # -> 228

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

#choose_best_sum(230, 4, xs) # -> 230
#choose_best_sum(430, 5, xs) # -> 430
#choose_best_sum(430, 8, xs) # -> None

xt = [100, 76, 56, 44, 89, 73, 68, 56, 64,
      123, 2333, 144, 50, 132, 123, 34, 89]
#choose_best_sum(880, 8, xt) # -> 876
