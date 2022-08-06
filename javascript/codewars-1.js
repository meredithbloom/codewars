const descendingOrder = (n) => {
    let string = n.toString();
    let split = string.split('')
    let sortedArray = split.sort(function (a, b) { return b - a })
    let newString = sortedArray.join('')
    console.log(newString)
    return parseInt(newString)
}

// descendingOrder(472)
// descendingOrder(9425381)



var isSquare = function (n) {
    if (n === 0) {
        return true
    } else {
        let i = 1;
        while (i < n) {
            let squared = i ** 2
            if (squared === n) {
                return true
            } else {
                i++
            }
        }
        return false
    }
}

// console.log(isSquare(16))
// console.log(isSquare(25))
// console.log(isSquare(27))


function findOutlier(integers) {
    let evens = 0;
    let odds = 0;
    for (let i = 0; i < 3; i++) {
        if (Math.abs(integers[i]) % 2 === 0 || integers[i] === 0) {
            evens += 1;
        } else {
            odds += 1;
        }
    }
    if (evens > odds) {
        for (let i = 0; i < integers.length; i++) {
            if (Math.abs(integers[i]) % 2 === 1) {
                let outlier = integers[i];
                return outlier;
            }
        }
    } else {
        for (let i = 0; i < integers.length; i++) {
            if (Math.abs(integers[i]) % 2 === 0) {
                let outlier = integers[i];
                return outlier;
            }
        }
    }
}
    

// console.log(findOutlier([0, 1, 2]))
// console.log(findOutlier([1, 2, 3]))
// console.log(findOutlier([2, 6, 8, 10, 3]))
// console.log(findOutlier([0, 0, 3, 0, 0]))
// console.log(findOutlier([1, 1, 0, 1, 1]));
// console.log(findOutlier([2, -3, 0, 6, -8]));

function likes(names) {
    if (names.length === 0) {
        return "no one likes this";
    } else if (names.length === 1) {
        return `${names[0]} likes this`;
    } else if (names.length === 2) {
        return `${names[0]} and ${names[1]} like this`;
    } else if (names.length === 3) {
        return `${names[0]}, ${names[1]} and ${names[2]} like this`;
    } else {
        let num = names.length - 2;
        return `${names[0]}, ${names[1]} and ${num} others like this`;
    }
}

// console.log(likes([]))
// console.log(likes(['Peter']))
// console.log(likes(['Jacob', 'Alex']))
// console.log(likes(['Max', 'John', 'Mark']))
// console.log(likes(['Alex', 'Jacob', 'Mark', 'Max']))

function humanReadable(seconds) {
    //converts to hours, leftovers are seconds
    let remainingSeconds = seconds % 60;
    let minutes = (seconds - remainingSeconds) / 60;
    
    //converts minutes to hours, leftovers are minutes
    let remainingMinutes = minutes % 60;
    let hours = (minutes - remainingMinutes) / 60;

    //if there are hours, we need to remove value from minutes
    if (hours > 0) {
        let remainingMinutes = minutes - (60 * hours);

        if (remainingMinutes < 10) {
            remainingMinutes = `0${remainingMinutes}`;
        }

        if (remainingSeconds < 10) {
            remainingSeconds = `0${remainingSeconds}`;
        }

        if (hours < 10) {
            hours = `0${hours}`;
        }
        let time = `${hours}:${remainingMinutes}:${remainingSeconds}`;
        console.log(time)
        return time
    } else {
        if (remainingMinutes < 10) {
            remainingMinutes = `0${remainingMinutes}`;
        }
        if (remainingSeconds < 10) {
            remainingSeconds = `0${remainingSeconds}`;
        }
        let time = `00:${remainingMinutes}:${remainingSeconds}`;
        console.log(time);
        return time;
    }
    
}

// humanReadable(0);
// humanReadable(59)
// humanReadable(60)
// humanReadable(90)
// humanReadable(3599)
// humanReadable(3600)
// humanReadable(45296)
// humanReadable(86399)
// humanReadable(86400)
// humanReadable(359999)

function digital_root(n) {
    let splitNum = n.toString().split('')
    let sum = 0
    for (num of splitNum) {
        sum += parseInt(num);
    }
    if (sum.toString().split('').length > 1) {
        return digital_root(sum)
    } else if (sum.toString().split('').length === 1) {
        return sum
    }
}

// console.log(digital_root(16))
// console.log('------')
// console.log(digital_root(456))
// console.log('------')
// console.log(digital_root(578))
// console.log('------')
// console.log(digital_root(57899))



function sumMultiples(max) {
    sum = 0;
    for (let i = 1; i < max; i++) {
        //console.log(i)
        if (i % 3 === 0 || i % 5 === 0) {
            //console.log(i)
            sum += i;
        }
    }
    console.log(sum)
}

//sumMultiples(10)
//sumMultiples(1000)


function findUniq(arr) {
    let first = arr[0]
    let second = arr[1]
    let third = arr[2]
    if (first === second || second === third) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] !== second) {
                return arr[i]
            }
        }
    } else if (first === third) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] !== third) {
                return arr[i]
            }
        }
    }
}

//console.log(findUniq([ 1, 1, 1, 2, 1, 1 ]))
//console.log(findUniq([ 0, 0, 0.55, 0, 0 ]))

function uniqueInOrder(iterable){
    let uniqueArray = []
    if (Array.isArray(iterable)) {
        if (iterable && !iterable.length) {
            //console.log('empty array')
            return iterable
        } else if (iterable.length >= 1) {
            uniqueArray.push(iterable[0])
            for (let i = 1; i < iterable.length; i++){
                if (iterable[i] !== iterable[i - 1]) {
                    uniqueArray.push(iterable[i])
                    //console.log(uniqueArray)
                }
            }
        }
        return uniqueArray
    } else if (typeof (iterable) === 'string') {
        let splitString = iterable.split('')
        uniqueArray.push(iterable[0])
        for (let i = 1; i < iterable.length; i++){
            if (iterable[i] !== iterable[i - 1]) {
                uniqueArray.push(iterable[i])
                //console.log(uniqueArray)
            }
        }
        return uniqueArray
    }
}

// console.log(uniqueInOrder('AAAABBBCCDAABBB'))
// console.log(uniqueInOrder('ABBCcAD'))
// console.log(uniqueInOrder([1, 2, 2, 3, 3]))
// console.log(uniqueInOrder([]))
//uniqueInOrder([])
//console.log(uniqueInOrder())

// function dirReduc(arr) {
//     let reducedNS = 0
//     let reducedEW = 0
//     const newDir = []
//     if (arr.length > 0) {
//         for (let i = 0; i < arr.length; i++){
            
//         }
//     } else {
//         return "empty directions"
//     }
// }


// dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
// dirReduc(["NORTH", "WEST", "SOUTH", "EAST"])
// dirReduc(["NORTH", "SOUTH", "EAST", "WEST", "EAST", "WEST"])


function countSmileys(arr) {
    let smileyCount = 0
    const smileyPattern = new RegExp('[\:\;]+?[\-~][\)D]')
    for (smiley in arr) {
        if (smiley === RegExp('')) {
            
        }
    }
}



function narcissistic(value) {
    let nums = value.toString().split('')
    let sum = 0
    for (n of nums) {
        sum += parseInt(n)**nums.length
    }
    if (sum === value) {
        return true
    } else {
        return false
    }
}


narcissistic(7)
narcissistic(371)
narcissistic(543)
