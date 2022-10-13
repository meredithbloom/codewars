# Pete, the Baker - 5 kyu
# write a function which takes the recipe (object) and the available ingredients (also an object) and return the max number of cakes that pete can bake (integer). ingredients not present in objects can be counted as 0
from collections import Counter 

def cakes(recipe, available):
    recipe = Counter(recipe)
    ingredients = Counter(available)
    difference = Counter()
    for item, units in recipe.items():
        if ingredients[item] > 0:
        	difference[item] = ingredients[item]//units
        else:
            return 0
    low = difference.most_common()[:-2:-1]
    print(low)
    print(low[0][1])
            
    
    



recipe1 = {"flour": 500, "sugar": 200, "eggs": 1}
available1 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

recipe2 = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available2 = {"sugar": 500, "flour": 2000, "milk": 2000}

# cakes(recipe1, available1)
#cakes(recipe2, available2)