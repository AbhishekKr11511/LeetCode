link = 'https://leetcode.com/problems/number-of-employees-who-met-the-target/'


// Solution
//---------------------------------
const numberOfEmployeesWhoMetTarget = (hours, target) => {
    let count = 0
    for (let i = 0; i < hours.length; i++) {
        if(hours[i]>=target){
            count++
        }
    }
    return count
}
//---------------------------------
let result = numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2)
console.log(result)