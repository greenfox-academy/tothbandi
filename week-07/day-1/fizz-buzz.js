'use strict';

// Write a program that prints the numbers from 1 to 100.
// But for multiples of three print “Fizz” instead of the number
// and for the multiples of five print “Buzz”.
// For numbers which are multiples of both three and five print “FizzBuzz”.

for(let i = 1; i <= 100; i++){
    let fizzbuzz = '';
    if(i % 3 === 0){
        fizzbuzz += 'Fizz';
    }
    if(i % 5 === 0){
        fizzbuzz += 'Buzz';
    }
    if (fizzbuzz === ''){
        console.log(i);
    } else {
        console.log(fizzbuzz);
    }
}