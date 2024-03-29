// 5 kyu - Play with two strings
/*
Your task is to Combine two Strings. But consider the rule...

By the way you don't have to check errors or incorrect input values, everything is ok without bad tricks, only two input strings and as result one output string;-)...

And here's the rule:
Input Strings a and b: For every character in string a swap the casing of every occurrence of the same character in string b. Then do the same casing swap with the inputs reversed. Return a single string consisting of the changed version of a followed by the changed version of b. A char of a is in b regardless if it's in upper or lower case - see the testcases too.
I think that's all;-)...

Some easy examples:

Input: "abc" and "cde"      => Output: "abCCde" 
Input: "ab" and "aba"       => Output: "aBABA"
Input: "abab" and "bababa"  => Output: "ABABbababa"

a) swap the case of characters in string b for every occurrence of that character in string a
char 'a' occurs twice in string a, so we swap all 'a' in string b twice. This means we start with "bababa" then "bAbAbA" => "bababa"
char 'b' occurs twice in string a and so string b moves as follows: start with "bababa" then "BaBaBa" => "bababa"

b) then, swap the case of characters in string a for every occurrence in string b
char 'a' occurs 3 times in string b. So string a swaps cases as follows: start with "abab" then => "AbAb" => "abab" => "AbAb"
char 'b' occurs 3 times in string b. So string a swaps as follow: start with "AbAb" then => "ABAB" => "AbAb" => "ABAB".

c) merge new strings a and b
return "ABABbababa"
*/
var _ = require('lodash');

function swapCase(letter) {
    if (letter === letter.toUpperCase()) {
        return letter.toLowerCase()
    } else {
        return letter.toUpperCase()
    }
}

function counter(string) {
    let counter = {}
    for (let letter of string) {
        if (counter[letter.toLowerCase()]) {
            counter[letter.toLowerCase()] += 1
        } else {
            counter[letter.toLowerCase()] = 1
        }
    }
    return counter
}

function workOnStrings(a,b){
    let bCopy = "";
    let aCopy = "";
    let aLetters = counter(a);
    let bLetters = counter(b);
    // filter both dictionaries so only keys present in both counters will remain
    let sharedValues = _.intersection(Object.keys(aLetters), Object.keys(bLetters))
    for (let key of Object.keys(aLetters)) {
        if (!sharedValues.includes(key)) {
            delete aLetters[key]
        }
    }
    for (let key of Object.keys(bLetters)) {
        if (!sharedValues.includes(key)) {
            delete bLetters[key]
        }
    }
    // deal with string b
    //console.log(b, aLetters)
    for (let cur of b) {
        if (Object.keys(aLetters).includes(cur.toLowerCase())) {
            let numSwitches = aLetters[cur.toLowerCase()]
            let uppercaseLetter = cur.toUpperCase()
            if (numSwitches%2 !== 0) {
                bCopy = bCopy + swapCase(cur)
            } else {
                bCopy = bCopy + cur
            }
        } else {
            bCopy = bCopy + cur
        }
    }
    //console.log(bCopy)
    // deal with string a 
    //console.log(a, bLetters)
    for (let cur of a) {
        if (Object.keys(bLetters).includes(cur.toLowerCase())) {
            let numSwitches = bLetters[cur.toLowerCase()]
            let uppercaseLetter = cur.toUpperCase()
            if (numSwitches%2 !== 0) {
                aCopy = aCopy + swapCase(cur)
            } else {
                aCopy = aCopy + cur
            }
        } else {
            aCopy = aCopy + cur
        }
    }
    //console.log(aCopy)
    //console.log(aCopy+bCopy)
    return(aCopy+bCopy)
}

//workOnStrings("abc","cde");
workOnStrings("abcdeFgtrzw", "defgGgfhjkwqe"); // abcDeFGtrzWDEFGgGFhjkWqE
//workOnStrings("abcdeFg", "defgG");
//workOnStrings("abab", "bababa");
