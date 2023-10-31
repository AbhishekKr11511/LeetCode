link = 'https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/'


// Solution
//---------------------------------
const smallerNumbersThanCurrent = (nums) => {
    let output = []
    for (let i = 0; i < nums.length; i++) {
        let count = 0
        for (let j = 0; j < nums.length; j++) {
            if(nums[i]>nums[j]) count++
        }
        output.push(count)
    }
    return output
}
//---------------------------------
let result = smallerNumbersThanCurrent([8,1,2,2,3])
console.log(result)