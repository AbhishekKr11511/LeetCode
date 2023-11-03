link = 'https://leetcode.com/problems/truncate-sentence/'


// Solution
//---------------------------------
const truncateSentence = (s, k) => {
    let output = []
    let input = s.split(' ')
    for (let i = 0; i < k; i++) {
        output.push(input[i])
    }
    return output.join(' ')
}
//---------------------------------
let result = truncateSentence("Hello how are you Contestant", 4)
console.log(result)