
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
	
	
