
'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(saying) {
  this.saying = saying;
}

Animal.prototype.say = function(){
  console.log(this.saying);
}

let dog = new Animal("whou");
let cat = new Animal("meow");

dog.say();
cat.say();