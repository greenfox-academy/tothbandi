'use strict';

var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for(let i = 0; i < lineCount; i++){
    let pyramid = '';
    for(let j = 0; j < lineCount - i - 1; j++){
        pyramid += ' ';
    }
    for(let j = 0; j < i * 2 + 1; j++){
        pyramid += '*';
    }
    console.log(pyramid);
}