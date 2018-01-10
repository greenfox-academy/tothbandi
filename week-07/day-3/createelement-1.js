'use strict';

// Add an item that says 'The Green Fox' to the asteroid list.
// Add an item that says 'The Lamplighter' to the asteroid list.
// Add a heading saying 'I can add elements to the DOM!' to the .container.
// Add an image, any image, to the container.

let asteroids = document.querySelector('.asteroids');
let listItem1 = document.createElement('li');
let listItem2 = document.createElement('li');
listItem1.innerText = 'The Green Fox';
listItem2.innerText = 'The Lamplighter';
asteroids.appendChild(listItem1);
asteroids.appendChild(listItem2);
let heading = document.createElement('h1');
heading.innerText = 'I can add elements to the DOM!';
let continer = document.querySelector('.container');
continer.appendChild(heading);
let image = document.createElement('img');
image.setAttribute('src', 'assets/hyena-32.png');
continer.appendChild(image);