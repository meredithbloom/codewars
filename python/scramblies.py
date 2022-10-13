# Scramblies - 5kyu
# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
# Only lower case letters will be used (a-z). No punctuation or digits will be included. Performance needs to be considered.
from collections import Counter

def scramble(s1, s2):
	string1 = Counter(s1)
	string2 = Counter(s2)
	if string2 <= string1:
		return True
	else:
		return False
	

