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
