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







