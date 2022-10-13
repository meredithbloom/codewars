// Directions Reduction - 5 kyu

// Once upon a time, on a way through the old wild mountainous west,…
// … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

// Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!//


let test1 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
let test2 = ["NORTH", "WEST", "SOUTH", "EAST"]
let test3 = ["NORTH", "SOUTH", "EAST", "WEST", "EAST", "WEST"]


const dirs = {
		NORTH: 'SOUTH',
		SOUTH: 'NORTH',
		EAST: 'WEST',
		WEST: 'EAST'
	}



function dirReduc(arr) {
	//console.log(arr)
	// creating stack
	let reduced = []
	for (i = 0; i < arr.length; i++) {
		//console.log(i)
		if (reduced.length > 0) {
			// the most recent element in stack
			let top = reduced[reduced.length-1]
			// if current dir is opposite current top
			if (arr[i] === dirs[top]) {
				// remove from stack
				reduced.pop()
			} else {
				// otherwise, add to stack
				reduced.push(arr[i])
			}
		} else {
			// if there is nothing in the stack, add whatever comes next to it
			reduced.push(arr[i])
		}
		//console.log(reduced)	
	}
	console.log(reduced)
}

// dirReduc(test1)
// dirReduc(test2)
// dirReduc(test3)