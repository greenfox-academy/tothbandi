'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

let width = 5;
let height = 13;
let depth = 9;

console.log('Surface area: ' + 2 * (width * height + height * depth + depth * width));
console.log('Volume: ' + width + height + depth);