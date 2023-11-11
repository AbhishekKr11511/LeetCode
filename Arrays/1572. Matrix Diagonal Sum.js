link = 'https://leetcode.com/problems/matrix-diagonal-sum/'


// Solution
//---------------------------------
const diagonalSum = (mat) => {
    let elements = []
    let len = mat.length
    if(len===1){
        return mat[0][0]
    }
    for (let i = 0; i < len; i++) {
        if(i!==len-1-i){
            elements.push(mat[i][i])
            elements.push(mat[i][len-1-i])
        }
    }
    if(len%2!==0){
        elements.push(mat[Math.floor(len/2)][Math.floor(len/2)])
    }
    let sum =  elements.reduce((accumulator, item)=>{
        return accumulator + item
    },0)
    return sum
}
//---------------------------------
let result = diagonalSum([[1,2,3],
    [4,5,6],
    [7,8,9]])
console.log(result)