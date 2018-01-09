'use strict';
// - Create a variable named `aj`
//   with the following content: `[3, 4, 5, 6, 7]`
// - Reverse the order of the elements in `aj`
// 		- do it with the built in method
//		- do it with creating a new temp array and a loop
// - Print the elements of the reversed `aj`

let aj = [3, 4, 5, 6, 7];

console.log(aj.reverse());

function revArr(normal){
  let reversed = [];
  let len = normal.length;
  for(let i = 0; i < len; i++){
    reversed.push(normal.pop());
  }
  return reversed;
}

console.log(revArr(aj));