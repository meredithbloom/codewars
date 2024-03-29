# Next bigger number with same digits - 4 kyu

'''
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071

nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1

nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil

TOPICS:
strings, refactoring

'''
from itertools import permutations


def next_bigger(n):
    nums = list(map(lambda x: int(x), list(str(n))))
    length = len(nums)
    # check for conditions to return -1
    # single digit
    if length == 1:
        return -1
    # if all digits are the same
    if len(set(nums)) == 1:
        return -1
    # if already ordered from greatest to smallest
    if nums == sorted(nums, reverse=True):
        return -1
    # for smaller numbers
    if len(nums) < 5:
        perms = list(permutations(str(n), len(nums)))
        #print(perms)
        # create list of only those numbers that are larger than n from permutations list
        joined = sorted([int("".join(x)) for x in perms if int("".join(x)) > int(n)])
        #print(joined)
        if len(joined) > 0:
            return joined[0]
        else:
            return -1
    # for larger numbers we need to start traversing from right to left
    # start from right-most digit and traverse left until we find the first digit that is smaller than the digit next to it
    for i in range(length-1, 0, -1):
        if nums[i] > nums[i-1]:
            break
    
    if i == 1 and nums[i] <= nums[i-1]:
        return -1
        
    x = nums[i-1]
    smallest = i
    for j in range(i+1, length):
        if nums[j] > x and nums[j] < nums[smallest]:
            smallest = j
    nums[smallest], nums[i-1] = nums[i-1], nums[smallest]
    x = 0
    for j in range(i):
        x = x*10 + nums[j]
    nums = sorted(nums[i:])
    for j in range(length-i):
        x = x*10 + nums[j]
    return x
    
    


# print(next_bigger(12))
# print(next_bigger(513))
# print(next_bigger(531))
# print(next_bigger(2017))
# print(next_bigger(414))
# print(next_bigger(144))
#print(next_bigger(1234567890)) # 1234567908
#print(next_bigger(534976)) # 536479
print(next_bigger(6963))
print(next_bigger(294))
# 6963 -> 9366
# 294 -> 429