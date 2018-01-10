'use strict';

//  <p class="apple">apple</p>
//  <p class="balloon">balloon</p>
//  <p class="cat red-dot">cat</p>
//  <p>dolphin</p>

//  Does the third p have a red-dot class?
//  If so, alert 'OMG DOTS!'
//  If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
//  If the first p has an 'apple' class, replace cat's content with 'dog'
//  Make apple red by adding a .red class
//  Make balloon less balloon-like

let paragraphs = document.querySelectorAll('p');
let apple = document.querySelector('.apple');

if(paragraphs[2].classList.contains('red-dot')){
  alert('OMG DOTS!');
}
if(paragraphs[3].classList.contains('dolphin')){
  apple.innerText = 'pear';
}
if(paragraphs[0].classList.contains('apple')){
  paragraphs.forEach(function(item){
    if(item.classList.contains('cat')){
      item.innerText = 'dog';
    }
  });
}
paragraphs.forEach(function(item){
  if(item.classList.contains('apple')){
    item.classList.add('red');
  }
  if(item.classList.contains('balloon')){
    item.style.borderRadius = '10px';
  }
});
