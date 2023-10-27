link = 'https://leetcode.com/problems/power-of-two/'


// Solution
//---------------------------------
const isPowerOfTwo = (n) => {
    if(n===0){
        return false
    }
    else{
        if(n===1){
            return true
        }else if(n%2===0){
            return isPowerOfTwo(n/2)
        }else{
            return false
        }
    }
}
//---------------------------------
console.log(isPowerOfTwo(12))