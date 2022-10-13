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

// console.log(productFib(1))
// console.log(productFib(2))
// console.log(productFib(3))
// console.log(productFib(4))
// console.log(productFib(10))
// console.log(productFib(25))
// console.log(productFib(100))
// console.log(productFib(135))
// console.log(productFib(4895))
// console.log(productFib(5895))
// console.log(productFib(74049690))
// console.log(productFib(84049690))
// console.log(productFib(193864606))
