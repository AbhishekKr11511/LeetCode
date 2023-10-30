link = 'https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/'


// Solution
//---------------------------------
const kidsWithCandies = (candies,extraCandies) => {
    let result  = []
    let max = candies.reduce((accumulator, item)=>{
        return Math.max(accumulator, item)
    })
    console.log(max);
    for (let i = 0; i < candies.length; i++) {
        if((candies[i]+extraCandies) >= max){
            result.push(true)
        }else{
            result.push(false)
        }
    }
    return result
}
//---------------------------------
let result = kidsWithCandies([2,3,5,1,3], 3)
console.log(result)