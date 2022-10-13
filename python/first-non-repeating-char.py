# The first non-repeating character - 5 kyu

# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

from collections import Counter

def first_non_repeating_letter(string):
    orig_string = string
    string = string.lower()
    non_repeating_chars = []
    char_count = Counter(string)
    for char, count in char_count.items():
        if count == 1:
            non_repeating_chars.append(char)
    #print(non_repeating_chars)
    if len(non_repeating_chars) == 1:
        print(non_repeating_chars[0])
        return non_repeating_chars[0]
    elif len(non_repeating_chars) == 0:
        print("")
        return ""
    else:
        for char in list(orig_string):
            if char.lower() in non_repeating_chars:
                print(char)
                return char
    


simple1 = 'a'
simple2 = 'sTreSS'
simple3 = 'moonmen'         
letter_case = 'Go hang a salami, I\'m a lasagna hog!'
odd_chars = '~><#~><'
repeating = 'abba'
empty = ''

# first_non_repeating_letter(simple2)
# first_non_repeating_letter(odd_chars)
# first_non_repeating_letter(simple3)
# first_non_repeating_letter(letter_case)