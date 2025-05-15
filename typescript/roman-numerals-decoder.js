"use strict";
// 6 KYU
// Roman Numerals Decoder
Object.defineProperty(exports, "__esModule", { value: true });
exports.solution = solution;
var numeralDictionary = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'D': 500,
    'CM': 900,
    'M': 1000
};
function solution(roman) {
    // for a given roman numeral, convert it to a number
    // create a dictionary of roman numerals and their integer values
    // iterate through the roman numeral string
    // if the current numeral is less than the next numeral, add the current numeral to the total
    // if the current numeral is greater than the next numeral, subtract the current numeral from the total
    var total = 0;
    for (var i = 0; i < roman.length; i++) {
        var currentNumeral = roman[i];
        var nextNumeral = roman[i + 1];
        if (numeralDictionary[currentNumeral] < numeralDictionary[nextNumeral]) {
            total -= numeralDictionary[currentNumeral];
        }
        else {
            total += numeralDictionary[currentNumeral];
        }
    }
    console.log(total);
    return total;
}
solution('XXI'); // 21
solution('I');
solution('IV');
solution('MMVIII');
solution('MDCLXVI');
