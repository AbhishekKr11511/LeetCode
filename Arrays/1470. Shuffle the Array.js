link = 'https://leetcode.com/problems/shuffle-the-array/'


// Solution
//---------------------------------
const shuffle = (nums, n) => {
    let output = []
    for (let i = 0; i < n; i++) {
        output.push(nums[i])
        output.push(nums[n+i])
    }
    return output
}
//---------------------------------
let result = shuffle([2,5,1,3,4,7], 3)
console.log(result)