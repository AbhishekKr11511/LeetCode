let n = 9

const isPowerOfFour = (n) => {
    if(n!==0){
        if(n===1){
            return true
        }else if(n%4===0){
            return isPowerOfFour(n/4)
        }else{
            return false
        }
    }else{
        return false
    }
}

let isIt = isPowerOfFour(0)

console.log(isIt);