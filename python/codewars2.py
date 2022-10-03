# String Incrementer - 5 kyu VERSION 2
# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# foo-> foo1

# foobar23-> foobar24

# foo0042-> foo0043

# foo9-> foo10

# foo099-> foo100

import re

def increment_string(string):
    pattern1 = r"[0-9](?=[0-9]|$)"
    num_split = re.findall(pattern1, string)
    
    # first we need to find where the number starts
    #num_split.append(string[-1])
    print(num_split)
    #print(re.split(pattern, string))


#increment_string("foo")
increment_string("foobar123")
increment_string("foo0042")
#increment_string("foo9")
increment_string("foobar23")
increment_string("foo099")
increment_string("foobar00")
increment_string("foobar99")
increment_string("fo99obar99")

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

# Regex Password Validation - 5kyu
# You need to write regex that will validate a password to make sure it meets the following criteria:
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)
from re import search 

regex = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*\d)[^\W_]{6,}$'

# start of word - ^
# contains at least one lowercase letter - (?=.*?[a-z])
# contains at least one uppercase letter - (?=.*?[A-Z])
# contains at least one number - (?=.*?[0-9]) - or (?=.*\d)
# only alphanumeric - [A-Za-z\d] -or  [^\W_]
# at least 6 characters long - {6,}
# end of word - $


# search(regex, 'fjd3IR9')
# search(regex, 'ghdfj32')
# search(regex, 'DSJKHD23')


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

# Tic Tac Toe checker - 5kyu
# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:
'''
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
'''
# Function should return -1 if board is unfinished AND no one has won yet (if there are empty spaces), 1 if 'X' won, 2 if 'O' won, or 0 if it's a draw

def is_solved(board):
	pass






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
	


# Product of consecutive fibonacci numbers
# return if two consecutive fib numbers can be multiplied to equal product, including the consecutive fib numbers
# f(n) * f(n+1) = prod
# return [f(n), f(n+1), true/false]
def productFib(prod):
    print(prod)
    fibs = [0,1,1]
    if prod > 2:
        for i in range(3, prod+3):
            fibs.append(fibs[i-2]+fibs[i-1])
            new = fibs[len(fibs)-1]
            current = fibs[i-2]*fibs[i-1]
            if current == prod:
                return [fibs[i-2], fibs[i-1], True]
            elif current > prod:
                return [fibs[i-2], fibs[i-1], False]
    elif prod == 2:
        fibs.append(2)
        return [fibs[2], fibs[3], True]
    elif prod == 1:
        return [fibs[1], fibs[2], True]
    elif prod == 0:
        return [fibs[0], fibs[1], True]


# Human Readable Time
def make_readable(seconds): 
    def single_digit(time):
        if time < 10:
            return('0'+str(time))
        else:
            return(str(time))
    
    hours = seconds//3600
    minutes = (seconds%3600)//60
    secs = seconds-(hours*3600)-(minutes*60)
    print(single_digit(hours)+':'+single_digit(minutes)+':'+single_digit(secs))
    
    
    




# make_readable(0)
# make_readable(5)
# make_readable(60)
# make_readable(86399)
# make_readable(359999)













# Moving zeros to the end
def move_zeros(array):
    count = array.count(0)
    while 0 in array:
        array.remove(0)
    for i in range(count):
        array.append(0)
    return(array)


# move_zeros([1, 0, 1, 2, 0, 1, 3])





# Did I finish my Sudoku?

def done_or_not(board):
    nums = [1,2,3,4,5,6,7,8,9]



















#--------------------------------------#

# PIG LATIN 
def pig_it(text):
    if len(text) == 0:
        return ''
    else:
        new = []
        words = text.split(' ')
        for word in words:
            if word.isalpha():
                word = word[1:]+word[0]+'ay'
                new.append(word)
            else:
                new.append(word)
        return " ".join(new)
        #print(new)

# print(pig_it('Pig latin is cool'))
# print(pig_it('Hello world !'))

#------------------------------------#

# ROT13
import string
def rot13(message):
    
    def convert(alphabet_list, letter):
        index = alphabet_list.index(letter)
        new_index = index+13
        if new_index >= 26:
            new_index -= 26
        letter = alphabet_list[new_index]
        return letter
    new_string = ''
    lowercase = list(string.ascii_lowercase)
    #print(lowercase)
    uppercase = list(string.ascii_uppercase)
    #print(uppercase)
    letters = list(message)
    for letter in letters:
        if letter.isalpha() and letter.islower():
            new_string += convert(lowercase, letter)
        elif letter.isalpha() and letter.isupper():
            new_string += convert(uppercase, letter)
        else:
            new_string+=letter
    print(new_string)
    return new_string

# rot13('test')
# rot13('Test')
# rot13('Codewars')
# rot13('d')