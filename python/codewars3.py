# Multiplication Table - 6 kyu
# Your task is to create an NxN multiplication table, of size provided in parameter

size1 = 3
size2 = 4

def multiplication_table(size):
    #table = []
    if size == 0:
        return -1
    max_num = size*size
    step = size
    start = 0
    table = [x for x in range(1,max_num+1)]
    tables = []
    #print(table)
    for i in range(start, max_num, step):
        x = i
        tables.append(table[x:x+step])
    print(tables)
        
    
    
        
        
multiplication_table(size1)
multiplication_table(size2)     


# Human readable duration format - 4 kyu
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

#  For seconds = 62, your function should return:
# "1 minute and 2 seconds"
# For seconds = 3662, your function should return:
# "1 hour, 1 minute and 2 seconds"
# https: // www.codewars.com/kata/52742f58faf5485cae000b9a/train/python for more details

def format_duration(seconds):
    if seconds == 0:
        return "now"
    # check for years
    elif seconds > 31535999:
        dys = seconds//86400
        yrs, rem_days = years(dys)
        format_plural(yrs, 'year')
        if rem_days > 0:
            format_plural(rem_days, 'day')
     # check for days
    elif seconds > 86399:
        hrs = seconds//3600
        dys, rem_hours = days(hrs)
        format_plural(dys, 'day')
        if rem_hours > 0:
            format_plural(rem_hours, 'hour')
    # check for hours
    elif seconds > 3599:
        mins = seconds//60
        hrs, rem_mins = hours(mins)
        format_plural(hrs, 'hour')
        if rem_mins > 0:
            format_plural(rem_mins, 'minute')
    # check for minutes
    elif seconds > 59:
        mins, rem_secs = minutes(seconds)
        format_plural(mins, 'minute')
        if rem_secs > 0:
            format_plural(rem_secs, 'second') 
    # check for seconds
    elif seconds < 60:
        format_plural(seconds, 'second')


def format_plural(count, time_unit):
    if count > 1:
        print(f'{count} {time_unit}s')
        return(f'{count} {time_unit}s')
    else:
        print(f'{count} {time_unit}')
        return(f'{count} {time_unit}')

def minutes(seconds):
    # 60 seconds per minute
    minutes = seconds//60
    rem_seconds = seconds%60
    return minutes, rem_seconds

def hours(minutes):
    # 60 minutes per hour
    # 3600 seconds per hour
    hours = minutes//60
    rem_minutes = minutes%60
    return hours, rem_minutes

def days(hours):
    # 24 hours per day
    # 1440 minutes per day
    # 86,400 seconds per day
    days = hours//24
    rem_hours = hours%24
    return days, rem_hours

def years(days):
    # 365 days per year
    # 8,760 hours per year
    # 525,600 minutes per year
    # 31,536,000 seconds per year
    years = days//365
    rem_days = days%365
    return years, rem_days

dur1 = 1
dur2 = 62
dur3 = 120
dur4 = 3600
dur5 = 3662

#format_duration(dur1)
#format_duration(2)
#format_duration(dur2)
#format_duration(dur3)
#format_duration(dur4)
#format_duration(dur5)

# Maximum subarray sum - 5 kyu
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

seq = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    # for list with only negative values
    if len(list(filter(lambda x: x>0, arr))) == 0 or len(arr) == 0:
        return 0
    max_so_far = 0
    max_ending_here = 0
    for e in range(len(arr)):
        max_ending_here = max_ending_here + arr[e]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if (max_ending_here<0):
            max_ending_here = 0
    return max_so_far    
    
#print(max_sequence(seq))    
    

# Range Extraction - 4 kyu
# A format for expressing an ordered list of integers is to use a comma separated list of either: 
# individual integers,
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

#import more_itertools as more
from itertools import groupby

solution1 = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]

def solution(args):
    final = ''
    groups = []
    for key, group in groupby(enumerate(args), key=lambda x: x[0]-x[1]):
        gb = list(group)
        new = [x[1] for x in gb]
        groups.append(new)
    #print(groups)
    for group in groups:
        if len(group) > 2:
            string = str(group[0])+'-'+str(group[-1])+','
            final+=string
        elif len(group) == 2:
            string = str(group[0])+','+str(group[1])+','
            final+=string
        else:
            final+=str(group[0])+','
    print(final.strip(','))
    return final.strip(',')
            

    # for group in more.consecutive_groups(args):
    #     g = list(group)
    #     #print(g)
    #     if len(g) > 2:
    #         reduced = str(g[0])+'-'+str(g[-1])
    #         print(reduced)
    #         final += reduced+', '
    #         print(final)
    #     else:
    #         reduced = str(g[0])
    #         print(reduced)
    #         final += reduced+', '
    # print(final.strip(', '))
    # return final.strip(', ')


#solution(solution1)

# needs to return string in correct format


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

# Best Travel - 5 kyu

# John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

# Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?

# t = max sum of distances
# k = number of towns to visit
# ls = list of distances

import itertools
import re
from collections import Counter

def choose_best_sum(t, k, ls):
    # all permutations of k length sub-lists of distances
    # sum of each permutation
    # highest sum <= t
    filtered = sorted(filter(lambda x: x <= t, ls))
    if len(filtered) < k:
        return None
    combs = list(itertools.combinations(filtered, k))
    sums = [sum(x) for x in combs]
    sums = list(filter(lambda x: x<=t, sums))
    if len(sums) == 0:
        return None
    return max(sums)
    

ls1 = [50, 55, 56, 57, 58]
#choose_best_sum(163, 3, ls1) # -> 163


ls2 = [50]
#choose_best_sum(163, 3, ls2) # -> null

ls3 = [91, 74, 73, 85, 73, 81, 87] 
#choose_best_sum(230, 3, ls3)  # -> 228

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

#choose_best_sum(230, 4, xs) # -> 230
#choose_best_sum(430, 5, xs) # -> 430
#choose_best_sum(430, 8, xs) # -> None

xt = [100, 76, 56, 44, 89, 73, 68, 56, 64,
      123, 2333, 144, 50, 132, 123, 34, 89]
#choose_best_sum(880, 8, xt) # -> 876

# Weight for weight - 5 kyu

# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.
# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

# Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

# when two numbers have the same "weight", let's class them as if they were strings (alphabetical ordering), and not numbers

def order_weight(strng):
    weights = sorted(strng.strip().split())
    w = sorted(weights, key=value)
    print(" ".join(w))
    return(" ".join(w))
    #print(weights)

def value(n):
    return sum([int(x) for x in n])


list1 = "56 65 74 100 99 68 86 180 90" # ordered by numbers
# should be -> "100 180 90 56 65 74 68 86 99"
list2 = "103 123 4444 99 2000"
list3 = "2000 10003 1234000 44444444 9999 11 11 22 123"
list4 = ""

#order_weight(list1)

# Most frequently used words in a text - 4kyu
'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

'''

string1 = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."





valid = (r'[a-zA-Z\']')


def check_char(char):
    if char.isalpha() or char == "'":
        return True
    else:
        return False



def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    #print(list(c))
    common = c.most_common(3)
    words = []
    for word in common:
        words.append(word[0])
    print(words)




# top_3_words(string1)

#top_3_words("a a a  b  c c  d d d d  e e e e e")
#top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# top_3_words("  //wont won't won't ")
# top_3_words("  '  ")
# top_3_words("  '''  ")
# top_3_words("LNHjcei-nBiKKCMgv -  LNHjcei-kepvNClzV!/;:_kDupSNELy?,: _QcibmQkHy,;_,,DARKdSL/. .!nBiKKCMgv//!!!DARKdSL!/LNHjcei//dLOFmmu'//_.yltqos .?;-kDupSNELy. ./nBiKKCMgv- ,_yltqos//._LNHjcei:_/dLOFmmu'__QcibmQkHy ?! LNHjcei!._QcibmQkHy,LNHjcei/.;LNHjcei_.;?yltqos:nBiKKCMgv:_ ./yltqos_ !LNHjcei-yltqos:!-?.yltqos :/nBiKKCMgv _!?QcibmQkHy-,:DARKdSL,!!;kDupSNELy,/ !!yltqos, :-kDupSNELy?-; _kDupSNELy/!kDupSNELy,_dLOFmmu'/--yltqos?yltqos-yltqos!-!yltqos!_?/_kDupSNELy_-!?kDupSNELy_!kDupSNELy?yltqos:LNHjcei yltqos/_ !kDupSNELy!!?kDupSNELy--.;-kDupSNELy?-kDupSNELy/!?;nBiKKCMgv./yltqos!/dLOFmmu'-,!:/kepvNClzV:dLOFmmu'.,??yltqos?_kDupSNELy?nBiKKCMgv./:-;LNHjcei ,.:kDupSNELy-kDupSNELy,yltqos!QcibmQkHy!kDupSNELy.nBiKKCMgv:..:kDupSNELy/yltqos,/.,LNHjcei/:!DARKdSL! ::?kepvNClzV_QcibmQkHy_/?/_kDupSNELy,_-nBiKKCMgv!///.kDupSNELy .yltqos:/;LNHjcei-:,?QcibmQkHy.!?.QcibmQkHy.LNHjcei  /yltqos._yltqos.?__LNHjcei/.?.kDupSNELy.!nBiKKCMgv!_: yltqos-dLOFmmu' kepvNClzV//_.?yltqos:nBiKKCMgv?;LNHjcei/nBiKKCMgv: ,kDupSNELy!;!:yltqos. .,:yltqos . ;yltqos/?,;;dLOFmmu'..:!nBiKKCMgv//DARKdSL.QcibmQkHy_:,./dLOFmmu'!dLOFmmu'_yltqos/.; nBiKKCMgv,-/_dLOFmmu'? dLOFmmu'._:..LNHjcei;/_dLOFmmu'!kDupSNELy -;;-kDupSNELy:.;?nBiKKCMgv,,yltqos,? ::dLOFmmu';-?;-LNHjcei/; ;_DARKdSL/? ??kDupSNELy:?QcibmQkHy, /nBiKKCMgv ?LNHjcei_- ::yltqos?_:;?kDupSNELy:!LNHjcei_,_?;")

# Permutations - 4kyu
# In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.
# Order of permutations doesn't matter


def permutations(s):
	print(s)
	combos = set(itertools.permutations(s))
	perms = ["".join(x) for x in combos]
	print(perms)


# permutations('a')
# permutations('ab')
# permutations('aabb')


