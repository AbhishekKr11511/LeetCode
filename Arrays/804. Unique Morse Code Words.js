link = 'https://leetcode.com/problems/unique-morse-code-words/'

// Morse Code for letters all 26 = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

// Solution
//---------------------------------
const uniqueMorseRepresentations = (words) => {
    output = ''
    let alphabets = 'abcdefghijklmnopqrstuvwxyz'
    let codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    let dict = []
    for (let i = 0; i < alphabets.length; i++) {
        dict.push({letter: alphabets[i], code: codes[i]})
    }
    console.log(dict);
    let wordscodearr = []
    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < dict.length; j++) {
            if(words[i]===dict[j].letter){
                wordscodearr.push(dict[j].code)
            }
        }
    }
    return wordscodearr.join(' ')
    
}
//---------------------------------
let result = uniqueMorseRepresentations('abhishek')
console.log(result)