'use strict';

// Turn the party on and off by clicking the button. (the whole page)

let button = document.querySelector('button');
let page = document.querySelector('div');
function letsParty() {
  page.classList.toggle('party');
}
button.addEventListener('click', letsParty);

