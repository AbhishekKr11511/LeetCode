link = 'https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/'


// Solution
//---------------------------------

const digitSum = (num) => {
    let mySum = String(num).split("").reduce((accumulator, ele)=> {
        return accumulator+Number(ele)
    },0)
    return mySum
}

const differenceOfSum = (nums) => {
    let sum = nums.reduce((accumulator, ele)=> {
        return accumulator+ele
    }, 0)
    let sumDigits = 0
    for (let i = 0; i < nums.length; i++) {
        sumDigits = sumDigits + digitSum(nums[i])
    }
    return(Math.abs(sum-sumDigits))
}
//---------------------------------

let result = differenceOfSum([1,15,6,3])
console.log(result)