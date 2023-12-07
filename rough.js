process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;                               // Reading input from STDIN
});

process.stdin.on("end", function () {
   main(stdin_input);
});

function check(num){
    let factors = []
    for(let i=1; i<= num/2;i++){
        if(num%i===0){
            factors.push(i)
        }
    }
    if (factors.length === 0){
        return "NO"
    }
    totalSum = factors.reduce((prev, curr)=>prev + curr)
    if(totalSum==num){
        return "YES"
    }
    else{
        return "NO"
    }
}

function main(input) {
    var result =[]
    var inputArray = input.split("\n")
    var testCases = inputArray.shift()

    for(let i = 0; i < testCases; i++){
        let temp = check(inputArray[i])
        result.push(temp)
    }
    var ans = result.join("\n")
    
    process.stdout.write(ans);       // Writing output to STDOUT
}