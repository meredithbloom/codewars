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

