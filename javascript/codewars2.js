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

function fib(n) {
	if (n < 2) {
		return n
	}
	return fib(n-1) + fib(n-2)
}

let cache = {
	'0': 0,
	'1': 1
}

function memoizedFib(n) {
	if (n in cache) {
		//console.log('pulling from cache...')
		return cache[n]
	}
	else if (n < 2) {
		//console.log(`first time calculating fib ${n}`)
		cache[n] = n
		return cache[n]
	}
	else {
		//console.log(`first time calculating fib ${n}`)
		cache[n] = fib(n-1) + fib(n-2)
	}
	//console.log(cache)
	return cache[n]
}

function productFib(prod) {
	// iterate through cache of fib numbers checking product of consecutive numbers
	if (prod === 3) {
		return [memoizedFib(3), memoizedFib(4), false]
	}
	else if (prod === 2) {
		return [memoizedFib(2), memoizedFib(3), true]
	}
	else if (prod === 1) {
		return [memoizedFib(1), memoizedFib(2), true]
	}
	for (let i = 1; i <= prod; i++) {
		if (memoizedFib(i - 1) * memoizedFib(i) === prod) {
			return [memoizedFib(i - 1), memoizedFib(i), true]
		} else if (memoizedFib(i - 1) * memoizedFib(i) > prod) {
			return [memoizedFib(i - 1), memoizedFib(i), false]
		}
	}
}

console.log(productFib(1))
console.log(productFib(2))
console.log(productFib(3))
console.log(productFib(4))
console.log(productFib(10))
console.log(productFib(25))
console.log(productFib(100))
console.log(productFib(135))
console.log(productFib(4895))
console.log(productFib(5895))
console.log(productFib(74049690))
console.log(productFib(84049690))
console.log(productFib(193864606))

// Take a Ten Minutes Walk - 6 kyu
/*
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
*/

function isValidWalk(walk) {
	let x = 0;
	let y = 0;
	if (walk.length !== 10) {
		return false
	}
	for (let step of walk) {
		if (step === 'n') {
			y++
		} else if (step === 's') {
			y--
		} else if (step === 'e') {
			x++
		} else if (step === 'w') {
			x--
		}
	}
	if (x !== 0 || y !== 0) {
		return false
	} else {
		return true
	}
}

let dir1 = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'];
let dir2 = ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'];

// console.log(isValidWalk(dir1))
// console.log(isValidWalk(dir2))





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

// console.log(seven(times(five())))
// console.log(eight(minus(three())))
// console.log(six(dividedBy(two())))

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