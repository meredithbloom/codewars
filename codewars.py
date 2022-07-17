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

       

generate_hashtag('')
generate_hashtag('Do We have A Hashtag')
generate_hashtag('Codewars')
generate_hashtag('Codewars      ')
generate_hashtag('Codewars Is Nice')
generate_hashtag('c i n')
generate_hashtag('codewars  is  nice')

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








