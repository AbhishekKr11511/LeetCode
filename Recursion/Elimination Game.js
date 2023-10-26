link = "https://leetcode.com/problems/elimination-game/";

// Solution
//---------------------------------


const lastRemaining = (n, asc = true, array = []) => {

    if(array.length===1){
        return array
    }
    else if(array.length!==0 && array.length!==1){
        if(asc === true){
            for (let i = 0; i <= array.length / 2; i++) {
                array[i] = array[2 * i + 1];
            }
            array.splice(array.length / 2, array.length);
            asc = !asc
            return lastRemaining(array.length/2, asc, array)
        }else{
            for (let i = array.length - 1; i >= array.length / 2; i--) {
                array[i] = array[2 * i - array.length];
            }
            array.splice(0, Math.ceil(array.length / 2));
            asc = !asc
            return lastRemaining(array.length/2, asc, array)
        }
    }
    else{
        for (let i = 1; i <= n; i++) {
            array.push(i);
        }
        return lastRemaining(n, asc, array)
    }
};
//---------------------------------

let value = lastRemaining(10)
console.log(value);
