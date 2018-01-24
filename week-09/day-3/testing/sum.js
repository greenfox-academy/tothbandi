'use strict';

function sum(numbers){
  if(Array.isArray(numbers)){
    if(numbers.length >= 1){
      return numbers.reduce((sum, value) => sum + value);
    } else {
      throw new Error('List is empty');
    }
  } else {
    throw new Error('Argument is not an array');      
  }
}

module.exports = {
  'sum': sum,
};