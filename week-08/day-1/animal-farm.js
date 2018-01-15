'use strict';

// Create an Animal constructor function
// Every animal has a hunger property, which is a number
// Every animal has a thirst property, which is a number
// When creating a new animal object these properties are created with the default 5 value
// Every animal can eat() which decreases their hunger by one
// Every animal can drink() which decreases their thirst by one
// Every animal can play() which increases both by one

function Animal() {
  this.hunger = 5,
  this.thirst = 5,
  this.eat = function() {
    this.hunger--;
    console.log('eats');
  },
  this.drink = function() {
    this.thirst--;
    console.log('drinks');
  },
  this.play = function() {
    this.hunger++;
    this.thirst++;
    console.log('plays');
  }
}

// Create a Farm constructor function
// The farm has slots which defines the number of free places for animals
// The farm has list of Animals
// The farm can breed() which creates a new animal if there's place for it
// The farm can slaughter() which removes the least hungry animal
// The farm can print reports about their current state:
// The farm has 11 living animals we are bankrupt
// The farm can progress from day to a new day by calling it's progress() method:
// All animals should have their methods called randomly with 50% chance
// The farm should call its breed and slaughter method at the end of each day
// The farm should print report at the end of each day

class Farm {

  constructor(slots) {
    this.freeSlot = slots;
    this.animals = [];
  }

  breed() {
    if(this.freeSlot > 0) {
      this.animals.push(new Animal());
      this.freeSlot--;
      console.log('New animal')
    } else {
      console.log('No more free slot');
    }
  }

  slaughter() {
    this.animals.sort((animal1, animal2) => {
      return animal1.hunger - animal2.hunger;
    });
    this.animals.shift();
    this.freeSlot++;
  }

  progress() {
    this.animals.forEach((animal, index, array) => {
      if(Math.random() < 0.5){
        animal.eat();
      }
      if(Math.random() < 0.5){
        animal.drink();
      }
      if(Math.random() < 0.5){
        animal.play();
      }
    });
    this.breed();
    this.slaughter();
    let population = this.animals.length;
    let message = '- The farm has ' + population + ' living animals, we are ';
    if(this.freeSlot === 0){
      message += 'full';
    } else if(population > 0 && this.freeSlot > 0){
      message += 'okay';
    } else if(population === 0){
      message += 'bankrupt'
    }
    console.log(message);
  }

}

// Print the number of sheeps
// Print "bankrupt" if no animals left
// Print "okay" if the number of animals is above zero and under the slot number
// Print "full" if the number of animals are at the maximum allowed

// Create a sheep farm with 20 slots
const SheepFarm = new Farm(20);

for (let i = 0; i < 20; i++){
  SheepFarm.breed();
}

console.log(SheepFarm.animals); // Should log 20 Animal objects

const button = document.querySelector('button');
button.addEventListener('click', SheepFarm.progress.bind(SheepFarm));

// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full