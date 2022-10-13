# The Observed PIN - 4kyu
# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8. the keypad has the following layout.
'''
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
'''
# Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. 
from itertools import permutations, product

buttons = {
		'0': ['0','8'],
		'1': ['1','2','4'],
		'2': ['1','2','3','5'],
		'3': ['2','3','6'],
		'4': ['1','4','5','7'],
		'5': ['2','4','5','6','8'],
		'6': ['3','5','6','9'],
		'7': ['4','7','8'],
		'8': ['0','5','7','8','9'],
		'9': ['6','8','9']
	}

def get_pins(observed):
    repeated = len(observed)
    keys = list(observed)
    combos = [buttons[key] for key in keys]
    #print(combos)
    possible = list(product(*combos, repeat=1))
    possible2 = [''.join(combo) for combo in possible]
    print(possible2)
        


# get_pins('8')
# get_pins('11')
# get_pins('369')

