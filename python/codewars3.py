# Permutations - 4kyu
# In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.
# Order of permutations doesn't matter
import itertools

def permutations(s):
	print(s)
	combos = set(itertools.permutations(s))
	perms = ["".join(x) for x in combos]
	print(perms)


permutations('a')
permutations('ab')
permutations('aabb')