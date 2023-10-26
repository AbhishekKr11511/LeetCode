let arr = [2,5,1,8,4,9,13]

const maximum = (array) => {
    let max = array[0]
    for (let i = 0; i < array.length; i++) {
        if(max < array[i]){
            max = array[i]
        }
    }
    return max
}

console.log(maximum(arr));