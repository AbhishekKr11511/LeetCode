link = 'https://leetcode.com/problems/shuffle-string/'


// Solution
//---------------------------------
const restoreString = (s, indices) => {
    let stringArr = s.split('')
    let outputArr = []
    console.log(stringArr);
    for (let i = 0; i < stringArr.length; i++) {
        for (let j = 0; j < stringArr.length; j++) {
            if(i==indices[j]){
                outputArr.push(stringArr[j])
                
            }
        }
    }
    return outputArr.join('')
}
//---------------------------------
let result = restoreString("codeleet", [4,5,6,7,0,2,1,3])
console.log(result)