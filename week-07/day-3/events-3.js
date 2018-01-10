'use strict';

// 1) Subscibe to keyup events on the global window object
// 2) Console log the event object and peek inside
// 3) Display the last pressed key's code as "Last pressed key code is: __"

let display = document.querySelector('h1')

function keyPressed(event){
  console.log(event);
  document.querySelector('h1').innerText = 'Last pressed key code is: ' + event.code;
}

window.addEventListener('keyup', keyPressed);