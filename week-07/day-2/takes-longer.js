
'use strict';
// When saving this quote a disk error has occured. Please fix it.
// Add "always takes longer than" to between the words "It" and "you"

var quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

let quoteArr = quote.split(' ');

let index = quoteArr.indexOf('It');

quoteArr.splice(index + 1, 0, 'always takes longer than');

quote = quoteArr.join(' ');

console.log(quote);