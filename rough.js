function check(num){
    let factors = []
    for(let i=1; i<= num/2;i++){
        if(num%i===0){
            factors.push(i)
        }
    }
    totalSum = factors.reduce((prev, curr)=>prev + curr)
    console.log(totalSum)
}

var func = function func(){
    console.log(func === func)
}
func()