'use strict';

var lineCount = 8;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

let upper = lineCount /= 2;
let lower = upper;

if(lineCount % 2 !== 0){
    lineCount += 0.5;
    lower = lineCount - 1;
}

for(let i = 0; i < upper; i++){
    let pyramid = '';
    for(let j = 0; j < upper - i - 1; j++){
        pyramid += ' ';
    }
    for(let j = 0; j < i * 2 + 1; j++){
        pyramid += '*';
    }
    console.log(pyramid);
}
for(let i = 0; i < lower; i++){
    let pyramid = '';
    if(lower < upper){
        pyramid += ' ';
    }
    for(let j = 0; j < i; j++){
        pyramid += ' ';
    }
    for(let j = 0; j < (lower- i) * 2 - 1; j++){
        pyramid += '*';
    }
    console.log(pyramid);
}
