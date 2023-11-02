link = 'https://leetcode.com/problems/left-and-right-sum-differences/'


// Solution
//---------------------------------
const leftRightDifference = (nums) => {
    let answer = []
    for (let i = 0; i < nums.length; i++) {
        let leftsum = nums.slice(0,i).reduce((carry, element)=>{
            return carry+element
        },0)
        let rightsum = nums.slice(i+1,nums.length).reduce((carry, element)=>{
            return carry+element
        },0)
        answer.push(Math.abs(leftsum-rightsum))
    }
    return answer
}
// //---------------------------------
let result = leftRightDifference([10,4,8,3])
console.log(result)

