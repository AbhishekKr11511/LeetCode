link = 'https://leetcode.com/problems/powx-n/'


// Solution
//---------------------------------
const myPow = (x,n, result = 1) => {
    if(n<0){
        return 1/myPow(x,-n, result)
    }
    if(n===0){
        return result
    }
    return myPow(x, n-1, result*x)
}
//---------------------------------
console.log(myPow(2, 2));