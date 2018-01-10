'use strict';

// fill output1 with the first paragraph's content, text only.
// fill output2 with the first paragraph's content keeping the cat strong.

let texts = document.querySelectorAll('p');
texts[1].innerText = texts[0].innerText;
texts[2].innerHTML = texts[0].innerHTML;