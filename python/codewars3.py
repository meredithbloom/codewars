# Permutations - 4kyu
# In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.
# Order of permutations doesn't matter
from itertools import combinations

def permutations(s):
	combos = combinations(s, len(s))
	print(combos)


permutations('a')
permutations('ab')
permutations('aabb')