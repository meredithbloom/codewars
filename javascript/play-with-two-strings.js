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
    //console.log(letter)
    if (letter === letter.toUpperCase()) {
        //console.log(letter, letter.toLowerCase())
        return letter.toLowerCase()
    } else {
        //console.log(letter, letter.toUpperCase())
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
    //console.log(aLetters)
    let bLetters = counter(b);
    //console.log(bLetters)
    // filter both dictionaries so only keys present in both counters will remain
    let sharedValues = _.intersection(Object.keys(aLetters), Object.keys(bLetters))
    console.log(sharedValues)
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
    console.log(aLetters)
    console.log(bLetters)
    // deal with string b - 
    console.log(b)
    for (let letter of Object.keys(aLetters)) {
        let numSwitches = aLetters[letter]
        let uppercaseLetter = letter.toUpperCase()
        //console.log(letter, uppercaseLetter)
        if (numSwitches%2 !== 0) {
            bCopy = b.replaceAll(letter, swapCase(letter))
            console.log(bCopy)
            bCopy = b.replaceAll(uppercaseLetter, swapCase(uppercaseLetter))
            console.log(bCopy)
        }
    }
    console.log(bCopy)
    // deal with string a 
}

//workOnStrings("abc","cde");
//workOnStrings("abcdeFgtrzw", "defgGgfhjkwqe");
workOnStrings("abcdeFg", "defgG");
//workOnStrings("abab", "bababa");