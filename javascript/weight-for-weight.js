// Weight for Weight - 5 kyu
/*
My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

NOTES
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers

*/


let weight1 = "56 65 74 100 99 68 86 180 90"; // -> "100 180 90 56 65 74 68 86 99"
let weight2 = "103 123 4444 99 2000"; // -> "2000 103 123 4444 99"
let weight3 = "2000 10003 1234000 44444444 9999 11 11 22 123" // -> ""11 11 2000 10003 22 123 1234000 44444444 9999""

function orderWeight(string) {
    let splitNums = string.split(" ")
    let weightDict = {}
    for (let num of splitNums) {
        let splitNum = num.split("").map(x => parseInt(x));
        let numSum = splitNum.reduce((previousValue, currentValue) => previousValue + currentValue, 0)
        if (weightDict[numSum]) {
            let curVal = weightDict[numSum]
            weightDict[numSum] = [...curVal, num]
        } else {
            weightDict[numSum] = [num]
        }
    }
    console.log(weightDict)

}



orderWeight(weight1)