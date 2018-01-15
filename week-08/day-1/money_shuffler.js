'use strict';
    
let flipflop = true;

let Shuffler = {
  cash: 10000,
  pick: function(){
    this.cash -= 1000;

    if (flipflop) {
      Panama.deposit(1000);
      flipflop = false;
    } else {
      Cyprus.deposit(1000);
      flipflop = true;
    }
  }
}

let Panama = {
  name: 'Panama',
  tax: '1%',
  cash: 0,
  deposit: function(amount){
    this.cash += amount;
    console.log(this.name + ' got ' + amount);
  }
}

let Cyprus = {
  name: 'Cyprus',
  tax: '5%',
  cash: 0,
  deposit: function(amount){
    this.cash += amount;
    console.log(this.name + ' got ' + amount);
  }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000