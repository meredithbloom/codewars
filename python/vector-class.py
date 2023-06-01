# 5 kyu
# Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])

# a.add(b)      # should return a new Vector([4, 6, 8])
# a.subtract(b) # should return a new Vector([-2, -2, -2])
# a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)      # raises an exception
# If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

# Also provide:

# a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
# an equals method, to check that two vectors that have the same components are equal
# Note: the test cases will utilize the user-provided equals method.

class Vector:

    # takes an array (vector) and initializes new vector
    def __init__(self, vals):
        self.vals = vals
        self.length = len(vals)
    
    def __str__(self):
        string = '('
        for i in range(0, self.length-1):
            string = string + str(self.vals[i]) + ','
        string = string[:-1]+')'
        return string

    # return a new vector with values from adding one vector to another
    def add(self, other_vector):
        if self.length != len(other_vector):
            raise ValueError('vectors are not of equal length')
        else:
            new_vector = []
            for i in range(0, self.length-1):
                new = self.vals[i] + other_vector[i]
                new_vector.append(new)
            return self.__init__(new_vector)

    # return a new vector with values from subtracting one vector from another
    def subtract(self, other_vector):
        if self.length != len(other_vector):
            raise ValueError('vectors are not of equal length')
        else:
            continue

    # find the sum of the products of two vectors
    def dot(self, other_vector):
        if self.length != len(other_vector):
            raise ValueError('vectors are not of equal length')
        else:
            continue

    # return the sqrt of the sums of the squares of all values in the vector
    def norm(self):
        total = 0
        for x in range(0, self.length-1):
            total += self.vals[0]**2
        return total**0.5