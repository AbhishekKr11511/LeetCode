link = 'https://leetcode.com/problems/n-repeated-element-in-size-2n-array/'
const _ = require('lodash')

// Solution
//---------------------------------
const repeatedNTimes = (nums) => {
    let count = 0
    let set = new Set(nums)
    let newSet = [...set]
    let diff = _.difference(nums, newSet)
    // const intersection = nums.filter(element => !newSet.includes(element));
    console.log(diff);
}
//---------------------------------
let result = repeatedNTimes([1,2,3,3])
// console.log(result)