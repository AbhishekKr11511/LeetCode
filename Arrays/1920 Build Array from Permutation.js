link = 'https://leetcode.com/problems/build-array-from-permutation/'


// Solution
//---------------------------------
const buildArray = (num) => {
    let output = []
    for (let i = 0; i < num.length; i++) {
        output.push(num[num[i]]) 
    }
    return output
}
//---------------------------------
const result = buildArray([0,2,1,5,3,4])
console.log(result);