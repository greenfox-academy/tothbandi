'use strict';
/* <section class="container">
<div id="b325" class="asteroid">The King</div>
<div class="asteroid b326">The Conceited Man</div>
</section>
<p class="asteroid big">The Businessman</p>
<div class="asteroid b329 big">The Lamplighter</div> */

// 1. store the element that says 'The King' in the 'king' variable.
// console.log it.
// <div id="b325" class="asteroid">The King</div>

let king = document.getElementById('b325');
console.log(king);

// 2. store the element that contains the text 'The Conceited Man'
// in the 'conceited' variable.
// show the result in an 'alert' window.
// <div class="asteroid b326">The Conceited Man</div>

let conceited = document.getElementsByClassName('b326');
alert(conceited[0].innerHTML);
console.log(conceited[0]);

conceited = document.querySelector('.b326');
alert(conceited.innerText);
console.log(conceited);

conceited = document.querySelectorAll('.b326');
alert(conceited[0].textContent);
console.log(conceited[0]);

// 3. store 'The Businessman' and 'The Lamplighter'
// in the 'businessLamp' variable.
// console.log each of them.
// <p class="asteroid big">The Businessman</p>
// <div class="asteroid b329 big">The Lamplighter</div>

let businessLamp = document.getElementsByClassName('big');
console.log(businessLamp);
for(let i = 0; i < businessLamp.length; i++){
  console.log(businessLamp[i]);
};

businessLamp = document.querySelectorAll('.big');
console.log(businessLamp);
businessLamp.forEach(item => console.log(item));

// 4. store 'The King' and 'The Conceited Man'
// in the 'conceitedKing' variable.
// alert them one by one.
// <section class="container">
// <div id="b325" class="asteroid">The King</div>
// <div class="asteroid b326">The Conceited Man</div>
// </section>

let conceitedKing = document.querySelectorAll('.container div');
conceitedKing.forEach(item => alert(item.innerHTML));

conceitedKing = document.getElementsByTagName('container div');
for(let i = 0; i < conceitedKing.length; i++){
  alert(conceitedKing[i]);
};

// 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
// in the 'noBusiness' variable.
// console.log each of them.
// <section class="container">
// <div id="b325" class="asteroid">The King</div>
// <div class="asteroid b326">The Conceited Man</div>
// </section>
// <p class="asteroid big">The Businessman</p>
// <div class="asteroid b329 big">The Lamplighter</div>
let noBusiness = document.getElementsByTagName('div');
for(let i = 0; i < noBusiness.length; i++){
  console.log(noBusiness[i]);
};

noBusiness = document.querySelectorAll('div');
noBusiness.forEach(item => console.log(item));

// 6. store 'The Businessman' in the 'allBizniss' variable.
// show the result in an 'alert' window.
// <p class="asteroid big">The Businessman</p>

let allBizniss = document.querySelector('p');
alert(allBizniss.innerHTML);

allBizniss = document.getElementsByTagName('p');
for(let i = 0; i < allBizniss.length; i++){
  alert(allBizniss[i].innerHTML);
};


