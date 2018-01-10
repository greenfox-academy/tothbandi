'use strict';
// <h1>Original Content</h1>
//  <p>Some more text</p>
//  <p class="other">Even more text</p>
//  <p class="result">Here comes something new</p>

//  <script>
//    1. Alert the content of the heading.
//    2. Write the content of the first paragraph to the console.
//    3. Alert the content of the second paragraph.
//    4. Replace the heading's content with 'New content'.
//    5. Replace the last paragraph's content with the first paragraph's content.
//  </script>

// 1.
let heading = document.querySelector('h1');
alert(heading.innerText);
// 2.
console.log(document.querySelector('p').innerText);
// 3.
alert(document.querySelector('.other').innerText);
// 4.
heading.innerText = 'New content';
// 5.
let paragraphs = document.querySelectorAll('p');
paragraphs[paragraphs.length-1].innerText = paragraphs[0].innerText;