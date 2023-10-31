link = 'https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/'


// Solution
//---------------------------------
const mostWordsFound = (sentences) => {
    let max = 0
    for (let i = 0; i < sentences.length; i++) {
        let temp = sentences[i].split(' ')
        if(temp.length > max){
            max = temp.length
        }
    }
    return max
}
//---------------------------------
let result = mostWordsFound(["please wait", "continue to fight", "continue to win"])
console.log(result)