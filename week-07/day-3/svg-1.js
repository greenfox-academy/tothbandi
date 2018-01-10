'use strict';

// 1) Select the rectangle by the ID: "very_rectangle"
// 2) Change the rectangle's position to x:50, y:50
// 3) Change its fill to tomato

let rect = document.getElementById('very_rectangle');
rect.setAttribute('x', '50');
rect.setAttribute('y', '50');
rect.style.fill = 'tomato';