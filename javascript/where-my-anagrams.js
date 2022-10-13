// Where my anagrams at? 5kyu
// Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none.


function anagrams(word, words) {
    let anagrams = []
    let newWords = words.filter(w => w.length === word.length)
    let original = word.split('').sort().join('')
    for (let w of words) {
        let temp = w.split('').sort().join('')
        if (original === temp) {
            anagrams.push(w)
        }
    }
    console.log(anagrams)
    return anagrams
}


// anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
// anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
// anagrams('laser', ['lazing', 'lazy', 'lacer'])
