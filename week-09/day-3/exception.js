'use strict';

// Handle the exceptions in the addString() function. It should check the type of the
// arguments, throw the right error and write it to the console.
// It should add the strings too if the arguments are appropriate.

let  addString = function(str1, str2, printStr){
  try {
    if (typeof str1 !== 'string' || typeof str2 !== 'string'){
      throw new Error('1st or 2nd argument is not string');
    };
    if (typeof printStr !== 'function'){
      throw new Error('Third argument is not a function');
    };
    let newStr = str1 + str2;
    printStr(newStr);
  } catch (error) {
    console.log(error.message);
  }

}

let printStr = function(str) {
  console.log(str);
}

addString(1234, 56789, 'printStr');
addString('1234', '56789', 'printStr');
addString('1234', '56789', printStr);