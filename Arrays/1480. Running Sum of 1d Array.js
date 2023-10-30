link = 'https://leetcode.com/problems/running-sum-of-1d-array/'


// Solution
//---------------------------------
const runningSum = (nums) => {
    let result = []
    for (let i = 0; i < nums.length; i++) {
        // let smallArray = nums.slice(0, i)
        // let sum = smallArray.reduce((acc, item)=>{
        //     return acc+item
        // },0)
        let sum = 0
        for (let j = 0; j <= i; j++) {
            sum = sum + nums[j]
        }
        
        result.push(sum)
    }
    return result
}
//---------------------------------
let result = runningSum([1,2,3,4])
console.log(result)