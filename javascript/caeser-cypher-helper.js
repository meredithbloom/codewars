// Caesar Cipher Helper - 5 kyu
// Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

//var c = new CaesarCipher(5); // creates a CipherHelper with a shift of five
//c.encode('Codewars'); // returns 'HTIJBFWX'
//c.decode('BFKKQJX'); // returns 'WAFFLES'

// If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
// The shift will always be in range of [1, 26].

class CaesarCipher {
    constructor(shift) {
        if (shift > 26 || shift < 1) {
            return 'invalid shift'
        }
        this.shift = shift
        this.alphabet = ['A','B','C','D','E','F','G','H','I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    }

    encode(stringToEncode) {
        const letters = stringToEncode.toUpperCase().split('')
        //console.log(letters)
        let newString = ''
        for (let letter of letters) {
            if (this.alphabet.includes(letter)) {
                let startIndex = this.alphabet.indexOf(letter)
                let newIndex = startIndex + this.shift
                if (newIndex > 25) {
                    newIndex -= 26
                }
                let newLetter = this.alphabet[newIndex]
                newString = newString+newLetter
            } else {
                newString = newString + letter
            }
        }
        console.log(newString)
        return newString
    }

    decode(stringToDecode) {
        const letters = stringToDecode.split('')
        let newString = ''
        for (let letter of letters) {
            if (this.alphabet.includes(letter)) {
                let startIndex = this.alphabet.indexOf(letter)
                let newIndex = startIndex - this.shift
                if (newIndex < 0) {
                    newIndex += 26
                }
                let newLetter = this.alphabet[newIndex]
                newString = newString + newLetter
            } else {
                newString = newString + letter
            }
        }
        console.log(newString)
        return newString
    }
}

var c = new CaesarCipher(5)
c.encode('Code wars') // 'HTIJBFWX'
c.decode('BFKKQJ,X'); // returns 'WAFFLES'