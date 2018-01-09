'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(number){
  let fact = 1;
  for(let i = 2; i <= number; i++){
    fact *= i;
  }
  if(number < 0){
    fact = 'The number must be non negative';
  }
  return fact;
}

console.log(factorio(0));
console.log(factorio(1));
console.log(factorio(5));
console.log(factorio(10));
console.log(factorio(-1));