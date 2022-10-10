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
        let remHundreds = num - thousands*1000
        return {thousands, remHundreds}
    }

    checkHundreds(num) {
        // number of whole hundreds
        let hundreds = Math.floor(num / 100)
        let remTens = num-hundreds*100
        return {hundreds, remTens}
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
            let romanNumeral = ''
            let { thousands, remHundreds } = this.checkThousands(num)
            let { hundreds, remTens } = this.checkHundreds(remHundreds)
            let { tens, remFives } = this.checkTens(remTens)
            let {fives, ones} = this.checkFives(remFives)
            console.log(`${thousands}000 + ${hundreds}00 + ${tens}0 + ${fives*5} + ${ones}`)
            let tally = [thousands*1000, hundreds*100, tens*10, fives*5, ones]
            for (let val of tally) {
                if (this.checkIfRoman(val)) {
                    //console.log(this.checkIfRoman(val))
                    romanNumeral += this.checkIfRoman(val)
                } else {
                    // calculate what roman numeral should be
                    console.log(val)
                }
            }
            console.log(romanNumeral)
        }
    }

    fromRoman(romanNum) {
        // if roman numeral is defined in base dictionary
        if (this.romanValues[romanNum]) {
            return this.romanValues[romanNum]
        }
        // we know there is at least 1000
        else if (romanNum.includes('M')) {

        }
    }

}

const RomanNumerals = new RomanNumeralsHelper()
//console.log(RomanNumerals.toRoman(1000))
//console.log(RomanNumerals.fromRoman('M'))

console.log(RomanNumerals.toRoman(1990))
console.log(RomanNumerals.toRoman(2008))
// RomanNumerals.fromRoman('XXI')
// RomanNumerals.fromRoman('IV')
// RomanNumerals.fromRoman('MMVIII')