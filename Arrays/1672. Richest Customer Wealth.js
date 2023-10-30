link = 'https://leetcode.com/problems/richest-customer-wealth/'


// Solution
//---------------------------------
const maximumWealth = (accounts) => {
    let richest = 0
    for (let i = 0; i < accounts.length; i++) {
        let sum = accounts[i].reduce((accumulator, currentValue) => {
            return accumulator + currentValue;
        }, 0)

        if(richest<sum){
            richest= sum
        }
    }
    return richest
}
//---------------------------------
let result = maximumWealth([[1,5],[7,3],[3,5]])
console.log(result)

let arr = [1,2,3,4,5]
arr.reduce((item)=> item)