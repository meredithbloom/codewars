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
