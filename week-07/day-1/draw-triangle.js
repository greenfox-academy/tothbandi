'use strict';

var lineCount = 4;

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is

for(let i = 0; i < lineCount; i++){
    let asterixes = ''
    for(let j = 0; j < i + 1; j++){
        asterixes += '*';
    }
    console.log(asterixes);
}