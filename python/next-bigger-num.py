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
    # check for conditions to return -1
    # single digit
    if len(nums) == 1:
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
        print(perms)
        # create list of only those numbers that are larger than n from permutations list
        joined = [int("".join(x)) for x in perms if int("".join(x)) > int(n)]
        #print(joined)
        if len(joined) > 0:
            return joined[0]
        else:
            return -1
    # for larger numbers we need to start flipping nums from right to left
    
    


print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(531))
print(next_bigger(2017))
print(next_bigger(414))
print(next_bigger(144))
print(next_bigger(1234567890))