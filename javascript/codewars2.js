// Product of consecutive Fib numbers - 5 kyu
/*
The Fibonacci numbers are the numbers in the following integer sequence (Fn):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
such as
F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:
[F(n), F(n+1), true]

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prod, you will return
[F(n), F(n+1), false]
F(n) being the smallest one such as F(n) * F(n+1) > prod.

*/

function productFib(prod) {
	let fibs = [0, 1, 1, 2];
	if (prod > 2) {
		
	}


}




// Calculating with Functions - 5 kyu
// This time we want to write calculations using functions and get the results. Let's have a look at some examples:
/*
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
*/
// Requirements:
/*
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
*/

function expression(num, operation) {
	if (!operation) {
		return num 
	} else {
		return operation(num)
	}
}

function zero(operation) {
	return expression(0, operation)
}
function one(operation) {
	return expression(1, operation)
}
function two(operation) {
	return expression(2, operation)
}
function three(operation) {
	return expression(3, operation)
}
function four(operation) {
	return expression(4, operation)
}
function five(operation) {
	return expression(5, operation)
}
function six(operation) {
	return expression(6, operation)
}
function seven(operation) {
	return expression(7, operation)
}
function eight(operation) {
	return expression(8, operation)
}
function nine(operation) {
	return expression(9, operation)
}

function plus(num) {
	return function (x) {
		return num + x
	}
}
function minus(num) {
	return function (x) {
		return x-num
	}
}
function times(num) {
	return function (x) {
		return num * x
	}
}
function dividedBy(num) {
	return function (x) {
		return Math.floor(x/num)
	}
}

console.log(seven(times(five())))
console.log(eight(minus(three())))
console.log(six(dividedBy(two())))

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