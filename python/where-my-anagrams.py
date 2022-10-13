# Where my anagrams at? 
# write a function that will find all the anagrams of a word from a list. two inputs - a word and an array of words. return an array of all the anagrams in the list or an empty array if there are none
from collections import Counter
def anagrams(word, words):
    counter = Counter(word)
    anagrams = []
    print(counter)
    for w in words:
        if len(w) == len(word):
            c = Counter(w)
            if len(counter-c) == 0:
                anagrams.append(w)
    print(anagrams)        
            

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
