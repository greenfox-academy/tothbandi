
'use strict';
// - Create a variable named `abc` with the following content: `["Arthur", "Boe", "Chloe"]`
// - Swap the first and the third element of `abc`

let abc = ["Arthur", "Boe", "Chloe"];

console.log(abc);

let element = abc[0];
abc[0] = abc[2];
abc[2] = element;

console.log(abc);
