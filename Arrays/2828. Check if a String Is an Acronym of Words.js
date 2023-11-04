link = 'https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/'


// Solution
//---------------------------------
const isAcronym = (words, s) => {
    let acronym = []
    for (let i = 0; i < words.length; i++) {
        acronym.push(words[i][0])
    }
    if(acronym.join('')===s){
        return true
    }else{
        return false
    }
}
//---------------------------------
let result = isAcronym(["alice","bob","charlie"], 'abc')
console.log(result)