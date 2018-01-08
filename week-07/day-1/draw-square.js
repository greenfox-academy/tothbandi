'use strict';

var lineCount = 6;

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

for(let i = 0; i < lineCount; i++){
    let line = '';
    if(i === 0 || i === lineCount - 1){
        for(let j = 0; j < lineCount; j++){
            line += '%';
        }
    } else {
        line += '%';
        for(let j = 0; j < lineCount - 2; j++){
            line += ' ';
        }
        line += '%';
    }
    console.log(line);
}