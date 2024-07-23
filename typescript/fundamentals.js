"use strict";
// 8 KYU
Object.defineProperty(exports, "__esModule", { value: true });
exports.Kata = exports.boolToWord = void 0;
exports.lovefunc = lovefunc;
exports.number = number;
// Convert boolean values to strings 'yes' or 'no' 
const boolToWord = (bool) => {
    // return bool ? 'Yes' : 'No';
    if (bool) {
        console.log('Yes');
        return 'Yes';
    }
    console.log('No');
    return 'No';
};
exports.boolToWord = boolToWord;
// boolToWord(true);
// boolToWord(false);
// Opposites attract
// write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't (if one is even and one is odd, they are in love, otherwise they are not)
function lovefunc(flower1, flower2) {
    // return flower1 % 2 != flower2 % 2;
    let flow1 = flower1 % 2 === 0 ? 'even' : 'odd';
    let flow2 = flower2 % 2 === 0 ? 'even' : 'odd';
    if (flow1 !== flow2) {
        return true;
    }
    return false;
}
// 7 KYU
// Testing 1-2-3
// write a function that takes a list of strings and returns each line prepended by the correct number - numbering starts at 1
// n: string
function number(array) {
    // array.map((el, i) => el = `${i+1}: ${el}`);
    let toReturn = [];
    for (let i = 0; i < array.length; i++) {
        let n = i + 1;
        toReturn.push(`${n}: ${array[i]}`);
    }
    return toReturn;
}
// Vowel count
// return the number (count) of vowels in a given string (a, e, i, o, u) - input string will only have spaces and/or letters
class Kata {
    static getCount(str) {
        const vowels = ['a', 'e', 'i', 'o', 'u'];
        let count = 0;
        for (let char of str.split('')) {
            console.log(char);
            if (vowels.includes(char)) {
                count++;
            }
        }
        console.log(count);
        return count;
    }
}
exports.Kata = Kata;
Kata.getCount("abracadabra");
