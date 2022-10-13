# Snail - 4 kyu
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
array1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
#snail(array)  # => [1,2,3,6,9,8,7,4,5]
array2 = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

array3 = [[]]
array4 = [[1]]

array5 = [[1, 2, 3, 4, 5], 
          [6, 7, 8, 9, 10], 
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20], 
          [21, 22, 23, 24, 25]]
# n x n matrix



def snail(snail_map):
    n = len(snail_map)
    if n == 1:
        return snail_map[0]
    snail = []
    top = 0
    bottom = len(snail_map)-1
    left = 0
    right = len(snail_map)-1
    #level = 0
    #r = 0
    # we want to stop when we know we have accounted for all numbers
    while len(snail) <= n*n:
        # first row (0 index), traverse from left to right
        for c in range(top,right+1):
            print(top, c)
            cur = snail_map[top][c]
            snail.append(cur)
        print('top row completed')
        top +=1
        if len(snail) == n*n:
            print(snail)
            return snail
        # last column (2 index), traverse from top to bottom
        for i in range(top, bottom+1):
            print(i, right)
            cur = snail_map[i][right]
            snail.append(cur)
        print('right side completed')
        right -= 1
        if len(snail) == n*n:
            print(snail)
            return snail
        # last row (2 index), traverse from right to left
        for c in range(right, left-1, -1):
            print(bottom, c)
            cur = snail_map[bottom][c]
            snail.append(cur)
        print('bottom row completed')
        bottom -= 1
        if len(snail) == n*n:
            print(snail)
            return snail
        # first columm (0 index), traverse from bottom to top
        for i in range(bottom, top-1,-1):
            print(i, left)
            cur = snail_map[i][left]
            snail.append(cur)
        print('left side completed')
        left += 1
        if len(snail) == n*n:
            print(snail)
            return snail
        print('loop completed')
        print(snail)
        #level += 1
    print(snail)
    return snail
    #pass

#snail(array1)

#snail(array2)

#snail(array5)
