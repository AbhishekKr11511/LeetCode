link = 'https://leetcode.com/problems/final-value-of-variable-after-performing-operations/'


// Solution
//---------------------------------
const finalValueAfterOperations = (operations) => {
    let x = 0
    for (let i = 0; i < operations.length; i++) {
        if(operations[i]==='X++' || operations[i]==='++X'){
            x = x + 1
        }else if(operations[i]==='X--' || operations[i]==='--X'){
            x = x - 1
        }
    }
    return x
}
//---------------------------------
let result = finalValueAfterOperations(["--X","X++","X++"])
console.log(result)