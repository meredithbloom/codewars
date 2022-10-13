
# Multiplication Table - 6 kyu
# Your task is to create an NxN multiplication table, of size provided in parameter

size1 = 3
size2 = 4

def multiplication_table(size):
    #table = []
    if size == 0:
        return -1
    max_num = size*size
    nums = []
    for row in range(1,size+1):
        cur = []
        for i in range(1,size+1):
            cur.append(row*i)
        nums.append(cur)
    print(nums)
    
        
    
    
        
        
#multiplication_table(size1)
#multiplication_table(size2)     

