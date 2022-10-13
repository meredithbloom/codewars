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
