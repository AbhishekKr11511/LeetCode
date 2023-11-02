link = 'https://leetcode.com/problems/decode-xored-array/'


// Solution
//---------------------------------
const decode = (encoded, first) => {
    let arr = [first]
    for (let i = 0; i < encoded.length; i++) {
        arr.push(arr[i] ^ encoded[i])
    }
    return arr
}
//---------------------------------
let result = decode([1,2,3], 1)
console.log(result)