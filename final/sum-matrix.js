'use strict';

const mockMatrix = [
  [1, 2, 3],
  [4, 5, 6]
];

const reducer = (accumulator, currentValue) => accumulator + currentValue;

function sumMatrix(matrix) {
  return matrix.map(row => row.reduce(reducer)).reduce(reducer);
}

console.log(sumMatrix(mockMatrix));
