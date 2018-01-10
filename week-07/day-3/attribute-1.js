'use strict';

// <img src="https://static.wixstatic.com/media/f4461b_83457ca5dd844c71a760d36e6583d0ff.png/v1/fill/w_168,h_168,al_c,usm_0.66_1.00_0.01/f4461b_83457ca5dd844c71a760d36e6583d0ff.png">
// <a href="http://www.themostamazingwebsiteontheinternet.com/">The Best Website Ever</a>
// <button>Click me!</button>
// <button class="this-one">Click me!</button>

// Write the image's url to the console.
//  Replace the image with a picture of your favorite animal.
//  Make the link point to the Green Fox Academy website.
//  Disable the second button.
//  Replace its text with 'Don't click me!'.

let image = document.querySelector('img');
console.log(image.getAttribute('src'));
image.setAttribute('src', 'assets/hyena-32.png');
document.querySelector('a').setAttribute('href', 'https://www.greenfoxacademy.com/');
let button = document.querySelector('.this-one');
button.setAttribute('disabled', 'disabled');
button.innerText = 'Don\'t click me!';

