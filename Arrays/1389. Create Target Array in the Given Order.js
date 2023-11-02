link = 'https://leetcode.com/problems/create-target-array-in-the-given-order/'


// Solution
//---------------------------------
const createTargetArray = (nums, index) => {
    target = []
    for (let i = 0; i < index.length; i++) {
        target.splice(index[i],0, nums[i])
    }
    return target
}
//---------------------------------
let result = createTargetArray([1,2,3,4,0], [0,1,2,3,0])
console.log(result)