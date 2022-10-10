// Roman Numerals Helper - 4 kyu

// Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

// Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

// input range - 1<= n < 4000


class RomanNumeralsHelper {
    romanValues = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    numeralValues = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    

    checkThousands(num) {
        // number of whole thousands, then remainder
        let thousands = Math.floor(num / 1000)
        let remFiveHundreds = num - thousands*1000
        return {thousands, remFiveHundreds}
    }

    checkFiveHundreds(num) {
        let fiveHundreds = Math.floor(num / 500)
        let remHundreds = num - fiveHundreds * 500
        return {fiveHundreds, remHundreds}
    }

    checkHundreds(num) {
        // number of whole hundreds
        let hundreds = Math.floor(num / 100)
        let remFifties = num-hundreds*100
        return {hundreds, remFifties}
    }

    checkFifties(num) {
        let fifties = Math.floor(num / 50)
        let remTens = num - fifties * 50
        return {fifties, remTens}
    }

    checkTens(num) {
        // number of whole tens
        let tens = Math.floor(num / 10)
        let remFives = num-tens*10
        return {tens, remFives}
    }

    checkFives(num) {
        let fives = Math.floor(num / 5)
        let ones = num - fives * 5
        return {fives, ones}
    }

    checkIfRoman(num) {
        if (this.numeralValues[num]) {
            return this.numeralValues[num]
        }
    }

    toRoman(num) {
        // if number is defined in base dictionary
        if (this.numeralValues[num]) {
            return this.numeralValues[num]
        }
        // check for thousands, hundreds, tens, ones
        else {
            console.log(num)
            let romanNumeral = ''
            let { thousands, remFiveHundreds } = this.checkThousands(num)
            let {fiveHundreds, remHundreds} = this.checkFiveHundreds(remFiveHundreds)
            let { hundreds, remFifties } = this.checkHundreds(remHundreds)
            // check if 900
            if ((hundreds * 100 + fiveHundreds * 500) === 900) {
                fiveHundreds = 0
                hundreds = 9
            }
            let { fifties, remTens } = this.checkFifties(remFifties)
            let { tens, remFives } = this.checkTens(remTens)
            // check if 90
            if ((tens * 10 + fifties * 50) === 90) {
                fifties = 0
                tens = 9
            }
            let { fives, ones } = this.checkFives(remFives)
            // check if 9
            if ((fives * 5 + ones === 9)) {
                fives = 0
                ones = 9
            }
            console.log(`${thousands}000 + ${fiveHundreds*500} + ${hundreds}00 + ${fifties*50} + ${tens}0 + ${fives*5} + ${ones}`)
            let tally = [thousands*1000, fiveHundreds*500, hundreds*100, fifties*50, tens*10, fives*5, ones]
            for (let val of tally) {
                if (this.checkIfRoman(val)) {
                    romanNumeral += this.checkIfRoman(val)
                } else {
                    // calculate what roman numeral should be. only need to check for base 10 nums
                    if (val === tally[0] && val > 0) {
                        let toAdd = 'M'.repeat(val / 1000)
                        romanNumeral += toAdd
                    } else if (val === tally[2] && val > 0) {
                        let toAdd = 'C'.repeat(val / 100)
                        romanNumeral += toAdd
                    } else if (val === tally[4] && val > 0) {
                        let toAdd = 'X'.repeat(val / 10)
                        romanNumeral+=toAdd
                    } else if (val === tally[6] && val > 0) {
                        let toAdd = 'I'.repeat(val)
                        romanNumeral+= toAdd
                    }
                }
            }
            //console.log(romanNumeral)
            return(romanNumeral)
        }
    }

    countFullNumerals(romanNum) {
        return romanNum.split('').reduce((map, char) => {
            return {
                ...map,
                [char] : (map[char] || 0) + 1
            }
        }, {})
    }

    halfVals = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

    countHalfNumerals(romanNum) {
        let halfValCount = {}
        for (let val of this.halfVals) {
            if (romanNum.match(val)) {
                halfValCount[val] = 1
            }
        }
        return halfValCount
    }

    fromRoman(romanNum) {
        // if roman numeral is defined in base dictionary
        if (this.romanValues[romanNum]) {
            return this.romanValues[romanNum]
        }
        // we have to calculate
        else {
        
            let totalVal = 0
            // check for half values
            let halfCount = this.countHalfNumerals(romanNum)
            let numeralCount = this.countFullNumerals(romanNum)
            console.log(halfCount)
            if (Object.keys(halfCount).length > 0) {
                let toSub = {}
                for (let key of Object.keys(halfCount)) {
                    totalVal += this.romanValues[key]
                    //console.log(totalVal)
                    let splitVals = key.split("")
                    for (let val of splitVals) {
                        if (toSub[val]) {
                            toSub[val] += 1
                        } else {
                            toSub[val] = 1
                        }
                    }
                }
                console.log(toSub)
                console.log(numeralCount)
                console.log(`counting only half values, value is ${totalVal}`)
                for (let key of Object.keys(numeralCount)) {
                    if (toSub[key]) {
                        numeralCount[key] -= toSub[key]
                    }
                }
            }
            console.log(numeralCount)
            for (let key of Object.keys(numeralCount)) {
                if (numeralCount[key] > 0) {
                    let toAdd = numeralCount[key] * this.romanValues[key]
                    console.log(toAdd)
                    totalVal += toAdd
                }
            }
            console.log(totalVal)
            return(totalVal)
        }
    }

}

const RomanNumerals = new RomanNumeralsHelper()
//console.log(RomanNumerals.toRoman(1000))
//console.log(RomanNumerals.fromRoman('M'))

//console.log(RomanNumerals.toRoman(1990))
//console.log(RomanNumerals.toRoman(2008))
//console.log(RomanNumerals.toRoman(4))
//console.log(RomanNumerals.toRoman(1666))
//RomanNumerals.fromRoman('XXI')
//RomanNumerals.fromRoman('IV')
//RomanNumerals.fromRoman('MMVIII')
//RomanNumerals.fromRoman('MDCLXVI')
RomanNumerals.fromRoman('MMDCCXLIX') // 2749
