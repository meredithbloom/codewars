// multiple of 3 or 5

function solution(number) {
    let multiples = []
    if (number < 0) {
        return 0
    } else {
        for (let i = 1; i < number; i++) {
            if ((i % 5 === 0) && (i % 3 === 0)) {
                multiples.push(i)
            } else if (i % 5 === 0) {
                multiples.push(i)
            } else if (i % 3 === 0) {
                multiples.push(i)
            }
        }
    }
    console.log(multiples)
    let sum = 0
    for (let num of multiples) {
        sum+=num
    }
    return sum
}

solution(10)
solution(23)
solution(15)


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

function dirReduc(arr) {
    let reducedNS = 0
    let reducedEW = 0
    const newDir = []
    if (arr.length > 0) {
        for (let i = 0; i < arr.length; i++){
            
        }
    } else {
        return "empty directions"
    }
}


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


// narcissistic(7)
// narcissistic(371)
// narcissistic(543)


function rgb(r, g, b) {
    if (r > 255) {
        r = 255
    } else if (r < 0) {
        r = 0
    }
    if (g > 255) {
        g = 255
    } else if (g < 0) {
        g = 0
    }
    if (b > 255) {
        b = 255
    } else if (b < 0) {
        b = 0
    }
    r = r.toString(16)
    if (r.length == 1) {
        r = '0' + r
    }
    g = g.toString(16)
    if (g.length == 1) {
        g = '0' + g
    }
    b = b.toString(16)
    if (b.length == 1) {
        b = '0' + b
    }
    let hex = r+g+b
    console.log(r + g + b)
    return hex.toUpperCase()
}
    

// rgb(0, 0, 0)
// rgb(300, 255, 255)
// rgb(173,255,47) 




function validParentheses(parens) {
    let stack = []
    for (let i = 0; i < parens.length; i++) {
        let current = stack[stack.length-1]
        if (parens[i] == "(") {
            stack.push(parens[i])
        } else if (current == "(" && parens[i] == ")") {
            stack.pop()
        } else {
            return false
        }
    }
    if (stack.length > 0) {
        return false
    } else {
        return true
    }
}


// validParentheses("(")
// validParentheses(")")
// validParentheses("")
// validParentheses("()")
// validParentheses("())")
// validParentheses("()(")


function validBraces(braces) {
    let stack = []
    for (let i = 0; i < braces.length; i++) {
        let current = stack[stack.length-1]
        if (braces[i] == "(" || braces[i] == "{" || braces[i] == "[") {
            stack.push(braces[i])
        } else if (current == "(" && braces[i] == ")") {
            stack.pop()
        } else if (current == "{" && braces[i] == "}") {
            stack.pop()
        } else if (current == "[" && braces[i] == "]") {
            stack.pop()
        } else {
            return false
        }
    }
    if (stack.length > 0) {
        return false
    } else {
        return true
    }
}

function sumStrings(a, b) {

    function checkZero(str) {
        if (str == '') {
            return 0
        } else {
            console.log(str)
            return str
        }
    }
    //console.log(parseInt(checkZero(a)))
    //console.log(parseInt(checkZero(b)))
    let sum = parseInt(checkZero(a)) + parseInt(checkZero(b))
    let fixed = Number.parseInt(sum)
    console.log(fixed)
    console.log(parseFloat(sum).toString())
}

//sumStrings('123', '456')
//sumStrings('', '5')
//sumStrings('712569312664357328695151392', '8100824045303269669937')
// 712577413488402631964821329

// var isPP = function (n) {
//     let max = n
//     for (let i = 2; i < n; i++) {
//         for (let j = 2; j < n; j++) {
//             if ((i ** j) == n) {
//                 return [i,j]
//             }
//         }
//     }
//     return null; // fix me
// }

var isPP = function (n) {
    let max = n
    if (Math.sqrt(n)) 
    for (let i = 2; i < n; i++) {
        for (let j = 2; j < 11; j++) {
            if ((i ** j) == n) {
                return [i,j]
            }
        }
    }
    return null; // fix me
}

// console.log(isPP(4))
// console.log(isPP(9))
// console.log(isPP(5))

class RomanNumerals {
    romanNumerals = {
        I: 1,
        IV: 4,
        V: 5,
        X: 10,
        L: 50,
        D: 100,
        M: 1000
    }

    numeralValues = {
        1: 'I',
        4: 'IV',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'D',
        1000: 'M'
    }

    toRoman = (integer) => {
        let numeralString = ''
        let currentRemainder = 0
        let thousands = Math.floor(integer / 1000)
        currentRemainder = integer - (thousands*1000)
        //console.log(thousands)
        let hundreds = Math.floor((integer - thousands*1000)/100)
        //console.log(hundreds)
        let fifties = Math.floor((integer - hundreds*100)/100)

    }

    fromRoman = (string) => {
        let roman = 0
        for (let i = 0; i < string.length; i++){
            if (string[i] + string[i + 1] == 'IV') {
                let value = this.romanNumerals['IV']
                roman += value
            } else {
                let value = this.romanNumerals[string[i]]
                roman += value
            }
        }
        //console.log(roman)
        this.romanValue = roman
        return roman
    }
}

const numeral = new RomanNumerals()
// console.log(numeral.fromRoman('MIV'))
// console.log(numeral.romanValue)
// console.log(numeral.toRoman(2500))


function pigIt(str) {
    let splitString = str.split(" ")
    //console.log(splitString)
    let newArray = []
    for (word of splitString) {
        //console.log(word)
        if (word.match(/[.,:!?]/)) {
            newArray.push(word)
        } else {
            let newWord = word.replace(/\W/, "")
            //console.log(newWord)
            let pigLatin = newWord.slice(1, word.length) + word[0] + 'ay'
            newArray.push(pigLatin)
            //console.log(newArray)
        }
    }
    joinedString = newArray.join(" ")
    return joinedString
}

//console.log(pigIt('Pig latin is cool !'))
//console.log(pigIt('This is my string !'))


function generateHashtag (str) {
    let trimmed = str.trim()
    if (trimmed.length == 0) {
        return false
    } else {
        let wordList = trimmed.split(" ")
        // console.log(wordList)
        let hashtag = "#"
        for (word of wordList) {
            let lowercase = word.toLowerCase()
            let capitalized = lowercase.charAt(0).toUpperCase() + lowercase.slice(1)
            hashtag += capitalized
        }
        //console.log(hashtag)
        if (hashtag.length > 140) {
            return false
        } else {
            return hashtag
        }
    }
}

// console.log(generateHashtag("Do We have A Hashtag"))
// console.log(generateHashtag("Codewars"))
// console.log(generateHashtag("Codewars Is Nice"))
// console.log(generateHashtag("code" + " ".repeat(140) + "wars"))
// console.log(generateHashtag(" ".repeat(200)))
// console.log(generateHashtag(""))

function alphanumeric(string) {
    if (string.length < 1) {
        return false
    }
    const regex = /[^A-Za-z0-9]/
    let found = string.match(regex)
    return (found ? false: true)
}

// console.log(alphanumeric("Mazinkaiser"))
// console.log(alphanumeric("hello world_"))
// console.log(alphanumeric("PassW0rd"))
// console.log(alphanumeric("     "))

function solution(list){
    let consecs = []
    let numString = ''
    for (let i = 0; i < list.length; i++) {
        consecs.push(list[i])
        if (list[i + 1] - list[i] > 1 && consecs.length == 1) {
            consecs = []
            numString += list[i].toString() + ','
        } else if (list[i + 1] - list[i] > 1 && consecs.length > 2) {
            let consecString = consecs[0].toString() + '-' + consecs[consecs.length - 1].toString() + ","
            numString += consecString
            consecs = []
        } else if (list[i + 1] - list[i] > 1 && consecs.length == 2) {
            numString += consecs[0].toString() + ',' + consecs[1].toString() + ","
            consecs=[]
        }
        // console.log(consecs)
        // console.log(numString)
    }
    if (consecs.length > 2) {
        console.log(consecs)
        let consecString = consecs[0].toString() + '-' + consecs[consecs.length - 1].toString()
        numString += consecString
    } else if (consecs.length == 1) {
        let consecString = consecs[0].toString()
        numString += consecString
    } else if (consecs.length == 2) {
        let consecString = consecs[0].toString() + ',' + consecs[1].toString()
        numString+=consecString
    }
    console.log(numString)
}

// solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
// solution([-71,-69,-66,-65,-64,-63,-61,-59,-57,-54,-53,-52,-49,-46,-43,-40,-37,-36,-35,-32,-30,-28,-25])