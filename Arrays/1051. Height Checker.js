link = 'https://leetcode.com/problems/height-checker/'


// Solution
//---------------------------------
const heightChecker = (heights) => {
    let sorted = [...heights]
    heights.sort()
    console.log(heights);
    let count = 0
    for (let i = 0; i < heights.length; i++) {
        if(heights[i]!==sorted[i]) count++
    }
    return count
}
//---------------------------------
let result = heightChecker([10,6,6,10,10,9,8,8,3,3,8,2,1,5,1,9,5,2,7,4,7,7])
console.log(result)
