link = ''
// Find the HCF of the following number


// Solution
//---------------------------------
const hcf = (num1, num2) => {
    let fact1 = []
    let fact2 = []
    for (let i = num1; i > 1; i--) {
        if(num1%i===0){
            fact1.push(i)
        }
    }
    for (let i = num2; i > 1; i--) {
        if(num2%i===0){
            fact2.push(i)
        }
    }
    console.log(fact1);
    console.log(fact2);

    for (let k = 0; k < fact1.length; k++) {
        for (let l = 0; l < fact2.length; l++) {
            if(fact1[k]===fact2[l]){
                return fact1[k]
            }
        }
    }
}

function gcd(a, b) {
    if (b === 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}
// //---------------------------------

let result = gcd(30, 20)
console.log(result);
