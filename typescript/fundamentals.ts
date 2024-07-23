// 8 KYU

// Convert boolean values to strings 'yes' or 'no' 

export const boolToWord = (bool: boolean): string => {
  // return bool ? 'Yes' : 'No';
  if (bool) {
    console.log('Yes');
    return 'Yes';
  }
  console.log('No');
  return 'No';
}

// boolToWord(true);
// boolToWord(false);


// Opposites attract
// write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't (if one is even and one is odd, they are in love, otherwise they are not)

export function lovefunc(flower1: number, flower2: number): boolean {
  // return flower1 % 2 != flower2 % 2;
  let flow1 = flower1 % 2 === 0 ? 'even':'odd';
  let flow2 = flower2 % 2 === 0 ? 'even':'odd';
  if (flow1 !== flow2) {
    return true;
  }
  return false;
}


// 7 KYU

// Testing 1-2-3
// write a function that takes a list of strings and returns each line prepended by the correct number - numbering starts at 1
// n: string

export function number(array: string[]): string[] {
  // array.map((el, i) => el = `${i+1}: ${el}`);
  let toReturn: string[] = [];
  for (let i=0; i<array.length; i++) {
    let n = i+1;
    toReturn.push(`${n}: ${array[i]}`);
  }
  return toReturn;
}

// Vowel count
// return the number (count) of vowels in a given string (a, e, i, o, u) - input string will only have spaces and/or letters
export class Kata {
  static getCount(str: string): number {
    const vowels: string[] = ['a', 'e', 'i', 'o', 'u'];
    let count = 0;
    for (let char of str.split('')) {
      if (vowels.includes(char)) {
        count++;
      }
    }
    return count;
  }
}

Kata.getCount("abracadabra");


// 6 KYU

// Multiples of 3 or 5
// finish the solution so that it returns the sum of all the multiples of 3 or 5 BELOW the number passed in
// if the number is negative, return 0
// if a number if a multiple of BOTH 3 and 5, only count it once

export class Challenge {
  static solution(number: number) {
    let sum = 0;
    if (number < 4) {
      return sum;
    }
    for (let i = 3; i < number; i ++) {
      if (this.checkIfMultiple(i)) {
        sum+=i;
      }
    }
    return sum;
  }

  static checkIfMultiple(number: number): boolean {
    if (number % 5 === 0 || number % 3 === 0) {
      return true;
    }
    return false;
  }
}