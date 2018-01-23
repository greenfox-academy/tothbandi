'use strict';

class ElevatorController {
}

class ElevatorModel {

  constructor(maxFloor, maxPeople){
    this.maxFloor = maxFloor;
    this.maxPeople = maxPeople;
    this.people = 0;
    this.position = 0;
    this.direction = 'up';
  }

  addPeople(){
    if(this.people < this.maxPeople){
      this.people++;
    } else {
      console.log('T e is full');
    }
  }

  removePeople(){
    if (this.people > 0) {
      this.people--;
    } else {
      console.log('T e is empty')
    }
  }

  move(){
    if(this.direction === 'up') {
      this.position++;
    }
    if(this.direction === 'down') {
      this.position--;
    }
  }
}

class ElevatorView {

  constructor(maxFloor){
    this.maxFloor = maxFloor;
    this.floors = [];
    this.actFloor;
    this.createFloors();
  }
  createFloors(){
    const elevator = document.querySelector('.elevator');
    for (let i = 0; i < this.maxFloor; i++) {
      let floor = document.createElement('div');
      floor.classList.add('floor');
      // floor.setAttribute('data-level', this.floors - i - 1);
      elevator.appendChild(floor);
      this.floors.unshift(floor);
    }
    this.actFloor = 0;
    this.drawElevatorInFloor(0);
  }

  drawElevatorInFloor(people){
    let actFloor = this.floors[this.actFloor];
    actFloor.textContent = people;
    actFloor.classList.add('actual');
  }
}

let el = new ElevatorView(10);
// el.createFloors();;