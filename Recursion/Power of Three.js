link = "https://leetcode.com/problems/power-of-three/"



// Solution
//---------------------------------
const isPowerOfThree = (n) => {
    if(n!==0){
        if(n===1){
            return true
        }else if(n%3===0){
            return isPowerOfThree(n/3)
        }else{
            return false
        }
    }else{
        return false
    }
}
//---------------------------------

let isIt = isPowerOfThree(0)

console.log(isIt);