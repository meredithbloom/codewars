# String Incrementer - 5 kyu
# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# foo-> foo1

# foobar23-> foobar24

# foo0042-> foo0043

# foo9-> foo10

# foo099-> foo100

import re

def increment_string(string):
    pattern = r"[0-9]"
    num_split = re.findall(pattern, string)
    print(num_split)
    # if no numbers at all
    if len(num_split) == 0:
        new_num = 1
        new_string = string+str(1)
        print(new_string)
        return new_string
    num = int("".join(num_split))
    new_num = num + 1
    if num_split[-1] == '0':
        # if all leading zeros
        cutoff = string[:-len(str(new_num))]
        new_string = cutoff+'1'
        print(new_string)
        return new_string
    elif len(str(new_num)) == len(num_split):
        # if new number needs to replace leading zero
        num_start = re.search(pattern, string)
        start = num_start.span()[0]
        new_string = string[:start]+str(new_num)
        print(new_string)
    elif len(str(new_num)) < len(num_split):
        # if new number needs leading zeros
        num_start = re.search(r"[1-9]", string)
        start = num_start.span()[0]
        new_string = string[:start]+str(new_num)
        print(new_string)
    elif len(num_split) == 1:
        num_start = re.search(pattern, string)
        start = num_start.span()[0]
        new_string = string[:start]+str(new_num)
        print(new_string)
    return new_string

increment_string("foo")
increment_string("foobar123")
increment_string("foo0042")
increment_string("foo9")
increment_string("foobar23")
increment_string("foo099")
increment_string("foobar00")

# String Incrementer - 5 kyu VERSION 2
# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# foo-> foo1

# foobar23-> foobar24

# foo0042-> foo0043

# foo9-> foo10

# foo099-> foo100

import re

def increment_string(string):
    pattern1 = r"[0-9](?=[0-9]|$)"
    pattern2 = r"[0-9](?=\D)"
    # check if there are numbers within string (not at end)
    bad_nums = re.findall(pattern2, string)
    # if there are, we need to only look at portion of string AFTER those mid-string nums
    if len(bad_nums) > 0:
        bad_num = re.search(pattern2, string)
        bad_index = bad_num.span()
        sliced_string = string[bad_index[1]:]
        num_split = re.findall(pattern1, sliced_string)
    else:
        # if there are no bad nums, we can just look at whole string
        num_split = re.findall(pattern1, string)
    if len(num_split) == 0:
        # if string has no nums at the end, we just add 1
        new_string = string+'1'
        print(new_string)
        return new_string
    else:
        joined = int("".join(num_split))
        #print(num_split)
        new_num = joined + 1
        #print(new_num)
        if len(str(new_num)) < len(num_split):
            # if we need leading zeros
            zero_count = len(str(new_num))
            new_string = string[:-zero_count]+str(new_num)
            print(new_string)
            return new_string
        elif len(str(new_num)) > len(num_split):
            # if we carry over a zero, i.e. 99 -> 100
            start_ind = len(num_split)
            new_string = string[:-start_ind]+str(new_num)
            print(new_string)
            return new_string
        elif len(str(new_num)) == len(num_split):
            start_ind = len(num_split)
            new_string = string[:-start_ind]+str(new_num)
            print(new_string)
            return new_string
    
    
    
        
    #print(re.split(pattern, string))


increment_string("foo")
increment_string("foobar123")
increment_string("foo0042")
increment_string("foo9")
increment_string("foobar23")
increment_string("foo099")
increment_string("foobar00")
increment_string("foobar99")
increment_string("fo99obar99")
increment_string("")