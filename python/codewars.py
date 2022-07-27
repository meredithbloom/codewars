# Sudoku Solution Validator - 4 kyu
'''
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
'''
from collections import Counter

def valid_solution(board):
    rows = {}
    columns = {}
    boxes = {}
    
    
        
    
    
    
    for r in range(9):
        rows[r] = Counter(board[r])
        print(f'current row is row {r}, counter: {rows[r]}, list: {list(rows[r])}')
        if len(list(rows[r])) != 9:
            return False
        col = []
        for c in range(9):
            if board[c][r] == 0:
                return False
            col.append(board[c][r])   
        columns[r] = Counter(col)
        print(f'current col is col {r}, counter: {columns[r]}, list: {list(columns[r])}')
        print()
        if len(list(columns[r])) != 9:
            return False
    return True
        
    #print(rows)
    
    
    
print(valid_solution([
    [1, 2, 3, 4, 5, 6, 7, 8, 9], 
    [2, 3, 4, 5, 6, 7, 8, 9, 1], 
    [3, 4, 5, 6, 7, 8, 9, 1, 2], 
    [4, 5, 6, 7, 8, 9, 1, 2, 3], 
    [5, 6, 7, 8, 9, 1, 2, 3, 4], 
    [6, 7, 8, 9, 1, 2, 3, 4, 5], 
    [7, 8, 9, 1, 2, 3, 4, 5, 6], 
    [8, 9, 1, 2, 3, 4, 5, 6, 7], 
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
])) # false



# print(valid_solution([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ])) # true

# print(valid_solution([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 6, 2, 4, 8, 5, 9],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ])) # false



# print(valid_solution([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 0, 3, 4, 8],
#     [1, 0, 0, 3, 4, 2, 5, 6, 0],
#     [8, 5, 9, 7, 6, 1, 0, 2, 0],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 0, 1, 5, 3, 7, 2, 1, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ])) # false

# The Observed PIN - 4kyu
# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8. the keypad has the following layout.
'''
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
'''
# Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. 
from itertools import permutations, product

buttons = {
		'0': ['0','8'],
		'1': ['1','2','4'],
		'2': ['1','2','3','5'],
		'3': ['2','3','6'],
		'4': ['1','4','5','7'],
		'5': ['2','4','5','6','8'],
		'6': ['3','5','6','9'],
		'7': ['4','7','8'],
		'8': ['0','5','7','8','9'],
		'9': ['6','8','9']
	}

def get_pins(observed):
    repeated = len(observed)
    keys = list(observed)
    combos = [buttons[key] for key in keys]
    #print(combos)
    possible = list(product(*combos, repeat=1))
    possible2 = [''.join(combo) for combo in possible]
    print(possible2)
        


# get_pins('8')
# get_pins('11')
# get_pins('369')


# Pete, the Baker - 5 kyu
# write a function which takes the recipe (object) and the available ingredients (also an object) and return the max number of cakes that pete can bake (integer). ingredients not present in objects can be counted as 0
from collections import Counter 

def cakes(recipe, available):
    recipe = Counter(recipe)
    ingredients = Counter(available)
    difference = Counter()
    for item, units in recipe.items():
        if ingredients[item] > 0:
        	difference[item] = ingredients[item]//units
        else:
            return 0
    low = difference.most_common()[:-2:-1]
    print(low)
    print(low[0][1])
            
    
    



recipe1 = {"flour": 500, "sugar": 200, "eggs": 1}
available1 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

recipe2 = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available2 = {"sugar": 500, "flour": 2000, "milk": 2000}

# cakes(recipe1, available1)
#cakes(recipe2, available2)

# Valid Parentheses - 5kyu
# write a function that takes a string of parentheses, and determines if the order of parentheses is valid. the function should return true if valid, false if not

def valid_parentheses(string):
    stack = []
    if len(string) == 0:
        return True
    for element in string:
        if element == '(':
            stack.append(element)
        elif element == ')' and len(stack) > 0:
            stack.pop()
        elif element == ')' and len(stack) == 0:
            return False
    if len(stack) > 0:
        return False
    else: 
        return True
    
valid_parentheses("  (")
valid_parentheses(")test")
valid_parentheses("")
valid_parentheses("hi())(")
valid_parentheses("hi(hi)()")


# The first non-repeating character - 5 kyu


# The Hashtag Generator - 5 kyu
# all words must have first word capitalized, if final result is longer than 140 characters it must return false. if input or output is empty string, also return false
def generate_hashtag(s):
    if len(s.strip()) == 0:
        return False
    else:
        split_words = s.strip().split()
        new_string = '#'
        for i in range(len(split_words)):
            new_string += split_words[i].capitalize()
        if len(new_string) > 140:
            return False
        else:
            return(new_string)

       

# generate_hashtag('')
# generate_hashtag('Do We have A Hashtag')
# generate_hashtag('Codewars')
# generate_hashtag('Codewars      ')
# generate_hashtag('Codewars Is Nice')
# generate_hashtag('c i n')
# generate_hashtag('codewars  is  nice')

# Sum of Intervals - 4 kyu
# write a function that accepts an array of intervals, the the reuns the sum of all the interval lengths. overlapping intervals should only be counted once









# Where my anagrams at? 
# write a function that will find all the anagrams of a word from a list. two inputs - a word and an array of words. return an array of all the anagrams in the list or an empty array if there are none
from collections import Counter
def anagrams(word, words):
    counter = Counter(word)
    anagrams = []
    print(counter)
    for w in words:
        if len(w) == len(word):
            c = Counter(w)
            if len(counter-c) == 0:
                anagrams.append(w)
    print(anagrams)        
            

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])

# RGB to Hex conversion
def rgb(r,g,b):
    def convert(decimal):
        if decimal > 255:
            decimal = 255
        elif decimal < 0:
            decimal = 0
        hexidecimal = hex(decimal)
        if len(hexidecimal[2:]) == 1:
            hexidecimal = '0'+hexidecimal[2:]
        else:
            hexidecimal = hexidecimal[2:]
        return hexidecimal.upper()
    
    red = convert(r)
    green = convert(g)
    blue = convert(b)
    rgb = red+green+blue
    print(rgb)


# rgb(0, 0, 0)
# rgb(1, 2, 3)
# rgb(255, 255, 255)
# rgb(254, 253, 252)
# rgb(-20, 275, 125)


# Directions Reduction

def dirReduc(arr):
	#print(arr)
	pairs = {
		'NORTH': 'SOUTH',
		'SOUTH': 'NORTH',
		'EAST': 'WEST',
		'WEST': 'EAST'
	}
	dirs = []
	for direction in arr:
		if dirs and pairs[direction] == dirs[-1]:
			dirs.pop()
		else:
			dirs.append(direction)
	return dirs
			


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# print(dirReduc(a))
u = ["NORTH", "WEST", "SOUTH", "EAST"]
# print(dirReduc(u))








#########
class User:
	ranks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]

	def __init__(self):
		self.rank_index = 0
		self.rank = self.ranks[self.rank_index]
		self.progress = 0


	def rank_up(self):
		if(self.progress>=100):
			print("adding " + str(self.progress)+ " points")
			levels_up = int(self.progress/100)
			remainder = self.progress % 100
			self.rank_index+=levels_up
			print("user will rank up " + str(levels_up) + " with a rollover value of " + str(remainder))
			self.progress = remainder
			self.rank = self.ranks[self.rank_index]
			print("new user rank is " + str(self.rank))
			if (self.rank == 8):
				self.progress = 0
		else:
			return


	def inc_progress(self, rank):
		#print("question is rank " + str(rank) + " and the user current has " + str(self.progress) + " points and is rank " + str(self.rank))
		if (rank in self.ranks):
			print("question is rank " + str(rank) + " and the user current has " + str(self.progress) + " points and is rank " + str(self.rank))
			if (self.rank == 8):
				print("you can't rank up anymore")
				self.progress+=0
				return
			elif (rank == self.rank):
				self.progress+=3
				print("current user rank is " + str(self.rank))
				print("adding " + str(self.progress)+ " points")
			elif(rank == self.ranks[self.rank_index-1] and rank != 8):
				self.progress+=1
				print("current user rank is " + str(self.rank))
				print("adding " + str(self.progress) + " points")
			elif(rank == self.ranks[self.rank_index-2] and rank != 8 and rank != 7):
				print("current user rank is " + str(self.rank))
				print("adding " + str(self.progress) + " points")
				self.progress+=0
			elif(rank > self.rank):
				d = rank-self.rank
				print("this question was " + str(d) + " ranks higher than user's current rank")
				if (rank > 0 and self.rank < 0):
					d-=1
				progress = 10*d*d
				print("question of " + str(d) + " ranks higher than user will add " + str(progress) + " points")
				self.progress += progress
				print("current user rank is " + str(self.rank))
				print("adding " + str(self.progress) + " points")
			self.rank_up()
		else:
			print(str(rank) + " is an invalid rank")
			return error





#user = User()
#print(user.rank)
#print(user)
#print(user.rank)
#user.rank
#user.inc_progress(3)
#print(user.rank)
#print(user.progress)
			
			
class User:
	ranks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]

	def __init__(self):
		self.rank_index = 0
		self.rank = self.ranks[self.rank_index]
		self.progress = 0


	def rank_up(self):
		if(self.progress>=100):
			levels_up = int(self.progress/100)
			remainder = self.progress % 100
			self.rank_index+=levels_up
			if (self.rank_index >= len(self.ranks)):
				self.rank_index[-1]
			self.progress = remainder
			self.rank = self.ranks[self.rank_index]
			if (self.rank == 8):
				self.progress = 0
		else:
			return


	def inc_progress(self, rank):
		print("question is rank " + str(rank) + " and the user current has " + str(self.progress) + " points and is rank " + str(self.rank))
		if (rank in self.ranks):
			if (self.rank == 8):
				self.progress+=0
				return
			elif (rank == self.rank):
				self.progress+=3
			elif(rank == self.ranks[self.rank_index-1] and rank != 8):
				self.progress+=1
			elif(rank == self.ranks[self.rank_index-2] and rank != 8 and rank != 7):
				self.progress+=0
			elif(rank > self.rank):
				d = rank-self.rank
				if (rank > 0 and self.rank < 0):
					d-=1
				progress = 10*d*d
				self.progress += progress
			self.rank_up()
		else:
			print(str(rank) + " is an invalid rank")
			return error
	
	
import math	
class PaginationHelper:
	
 	# The constructor takes in an array of items and a integer indicating
  	# how many items fit within a single page
	def __init__(self, collection, items_per_page):
		self.collection = collection 
		self.items_per_page = items_per_page
	  
   	# returns the number of items within the entire collection
	def item_count(self):
		return len(self.collection)
	  
   	
	# returns the number of pages
	def page_count(self):
		return math.ceil(self.item_count()/self.items_per_page)

	# returns the number of items on the current page. page_index is zero based
	# this method should return -1 for page_index values that are out of range
	def page_item_count(self, page_index):
		if page_index > (self.page_count()-1) or page_index < 0:
			return -1
		if self.item_count()%self.items_per_page == 0:
			return self.items_per_page
		elif self.item_count()%self.items_per_page != 0:
			if page_index == (self.page_count()-1):
				return self.item_count()%self.items_per_page
			else:
				return self.items_per_page
	   
  
	# determines what page an item is on. Zero based indexes.
	# this method should return -1 for item_index values that are out of range
	def page_index(self, item_index):
		if item_index > (self.item_count()-1) or item_index < 0:
			return -1
		if item_index == (self.item_count()-1):
			return self.page_count()-1
		else:
			return int(item_index/self.items_per_page)
  

# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# print(helper.page_count()) # 2 pages. 0 indexed, page 0, page 1
# print(helper.item_count()) # 
# print(helper.page_item_count(2)) # -1
# print(helper.page_item_count(1)) # 2
# print(helper.page_item_count(0)) # 4

# print(helper.page_index(20)) # -1
# print(helper.page_index(5))  # should == 1 (zero based index)
# print(helper.page_index(2))  # should == 0
# print(helper.page_index(-10))  # should == -1 because negative indexes are invalid








