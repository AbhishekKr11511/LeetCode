const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const arr = [];
// rl.question('What is your name : ', (name)=>{
//     console.log(`Hello ${name}`);
//     rl.close()
// })

let count = 0

rl.question("Enter number : ", (num) => {
  arr.push(num);
  count++
  if(count > 4){
    console.log(arr);
    rl.close()
  }
});

