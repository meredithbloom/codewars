// Pete, the baker - 5 kyu

// Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?
// Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

// cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}); --> returns 2 
// cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000});
// --> returns 0

function cakes(recipe, available) {
    let necessaryIngredients = Object.keys(recipe)
    let overlap = {}
    console.log(necessaryIngredients)
    necessaryIngredients.forEach((key, index) => {
        // check if available includes any of all ingredients
        if (!available[key]) {
            console.log(`no ${key} in available ingredients`)
            return 0
        // now need to compare recipe to available
        } else {
            let count = Math.floor(available[key] / recipe[key])
            overlap[key] = count
        }
    })
    let counts = Object.values(overlap)
    if (counts.length < necessaryIngredients.length) {
        console.log(`missing ingredients, can't make any cake`)
        return 0
    }
    let min = Math.min(...counts)
    console.log(min)
    return min
    
}

//cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200}); 
//cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000});