link = 'https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/'


// Solution
//---------------------------------
const arrayStringsAreEqual = (word1, word2) => {
    let str1 = word1.join('')
    let str2 = word2.join('')
    if(str1===str2){
        return true
    }else{
        return false
    }
}
//---------------------------------
let result = arrayStringsAreEqual(["ab", "c"],["a", "bc"])
console.log(result)