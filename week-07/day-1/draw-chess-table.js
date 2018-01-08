// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//

'use strict';

for(let i = 0; i < 8; i++){
    let line = '';
    for(let j = 0; j < 8; j++){
        if((i + j) % 2 === 0){
            line += '%';
        } else {
            line += ' ';
        }
    }
    console.log(line);
}