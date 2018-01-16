'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

let fruits = ['apple', 'pear', 'melon', 'grapes'];
fruits.forEach(function(fruit, index) {
  setTimeout(function(){console.log(fruit)}, (2 * index - 1) * 1000 );
});


