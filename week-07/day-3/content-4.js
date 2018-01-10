'use strict';

//    1) replace the list items' content with items from this list:
//    ['apple', 'banana', 'cat', 'dog']
//    2) change the <ul> element's background color to 'limegreen'
//      - don't just add a CSS class
//      - use the .style attribute

let contents = ['apple', 'banana', 'cat', 'dog'];
let items = document.querySelectorAll('li');
items.forEach( (item, index) => item.innerText = contents[index]);
document.querySelector('ul').style.backgroundColor = 'limegreen';