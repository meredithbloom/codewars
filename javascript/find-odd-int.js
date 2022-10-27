// Find the odd int - 6 kyu
/*
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
*/


function findOdd(A) {
    let counter = {}
    for (let num of A) {
        //console.log(num)
        if (counter[num] > 0) {
            counter[num]++
        } else {
            counter[num] = 1
        }
    }
    console.log(counter)
    for (let key of Object.keys(counter)) {
        if (counter[key] % 2 !== 0) {
            console.log(key)
            return parseInt(key)
        }
    }
}


const test1 = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
const test2 = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
const test3 = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
const test4 = [0, 1, 0, 1, 0]


findOdd(test1)
findOdd(test2)
findOdd(test3)
findOdd(test4)