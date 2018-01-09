'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer(a = '', b = '', c = ''){
  console.log(a);
  console.log(b);
  console.log(c);
  console.log('-------------');
}

let pear = 'a pear is another fruit'

printer();
printer('apple');
printer('apple', 5);
printer('apple', 5, pear);
printer('apple', 5, pear, 'valami');

function printAll(){
  let args = Array.from(arguments);
  args.forEach(function(item){
    console.log(item);
  });
  console.log('-------------');
}

printAll();
printAll('apple');
printAll('apple', 5);
printAll('apple', 5, pear);
printAll('apple', 5, pear, 'valami');