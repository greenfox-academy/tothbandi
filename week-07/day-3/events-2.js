'use strict';

// On the click of the button,
// Count the items in the list
// And display the result in the result element.

let button = document.querySelector('button');
let page = document.querySelector('div');
function countItems() {
  document.querySelector('p').textContent = document.querySelectorAll('li').length;
}
button.addEventListener('click', countItems);