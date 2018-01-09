
'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array

function createMatrix(size){
  let matrix = [];
  for(let i = 0; i < size; i++) {
    let row = [];
    for(let j = 0; j < size; j++){
      row.push(0);
      if(j === size - 1 - i){
        row[j] = 1;
      }
    }
    matrix.push(row);
  }
  return matrix;
}

console.log(createMatrix(10));

function printMatrix(matrix){
  matrix.map(function(item){
    let row = '';
    item.forEach(function(item){
      row += item + ' ';
    })
    console.log(row);
  })
}

printMatrix(createMatrix(10));