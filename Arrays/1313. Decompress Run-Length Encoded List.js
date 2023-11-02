link = 'https://leetcode.com/problems/decompress-run-length-encoded-list/'


// Solution
//---------------------------------
const decompressRLElist = (nums) => {
    let output = []
    // let freqVal = []
    for (let i = 0; i < nums.length; i=i+2) {
        // let obj = {
        //     freq : nums[i],
        //     value : nums[i+1]
        // }
        // freqVal.push(obj)
        for (let j = 0; j < nums[i]; j++) {
            output.push(nums[i+1])
        }
    }
    return output
}
//---------------------------------
let result = decompressRLElist([1,2,3,4])
console.log(result)