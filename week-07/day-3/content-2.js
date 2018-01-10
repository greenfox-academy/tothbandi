'use strict';

// fill every paragraph with the last one's content.

let things = document.querySelectorAll('p');
things.forEach(item => item.innerText = things[things.length - 1].innerText);
