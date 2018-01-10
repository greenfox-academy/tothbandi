'use strict';

// Remove the Mega juicy candy from the list.
// Add 16 list items saying 'Empty box' to the list and add an index to it, like:
// Empty box #1
// Empty box #2
// Empty box #3
// ...

let candyShop = document.querySelector('.candyshop');
let boxes = document.querySelectorAll('.candyshop li');
candyShop.removeChild(boxes[0]);
for(let i = 0; i < 16; i++){
  let box = document.createElement('li');
  box.innerText = 'Empty box #' + (i + 1);
  candyShop.appendChild(box);
}


