

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
    
    
    




make_readable(0)
make_readable(5)
make_readable(60)
make_readable(86399)
make_readable(359999)













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