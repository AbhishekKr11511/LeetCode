link = 'https://leetcode.com/problems/concatenation-of-array/'


// Solution
//---------------------------------
const getConcatenation = (nums) => {

    // 1 Solution
    // let output = []
    // output = [...nums, ...nums]
    // return output

    // 2 Solution
    let output = []
    for (let i = 0; i < nums.length; i++) {
        output.push(nums[i]);
    }
    for (let i = 0; i < nums.length; i++) {
        output.push(nums[i]);
    }
    return output
    
}
//---------------------------------
let result = getConcatenation([1,2,1])
console.log(result)

