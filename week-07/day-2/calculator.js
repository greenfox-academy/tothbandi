'use strict';
// Create a simple calculator application which does read the parameters from the standard input 
// and prints the result to the console.

// It should support the following operations: 
// +, -, *, /, % and it should support two operands. 

// The format of the expressions must be: {operation} {operand} {operand}. 
// Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

// You should use the command line arguments to accept user input

// It should work like this:

// Start the program with "node calculator.js + 5 6"
// If number of arguments are not correct, print some nice errors
// Else print the result
// Say goodbye

var args = process.argv.splice(2); // Just a helper for you to get started

console.log('Input params are', args);

if(args.length !== 3 || ['+', '-', '*', '/', '%'].indexOf(args[0]) === -1){
  console.log('Wrong arguments. Fromat must be: ');
  console.log('node calculator.js {operator} {operand} {operand}');
  console.log('operator must be in quotation mark: "+", "-", "*", "//", "%"');
} else {
  let expression = args[1] + ' ' + args[0] + ' ' + args[2];
  console.log(expression + ' = ' + eval(expression));
}
