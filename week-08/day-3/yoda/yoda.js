'use strict';
let body = document.querySelector('body');
let label = document.createElement('label');
label.textContent = 'Enter a sentence: '
let input = document.createElement('input');
input.type = 'text';
input.placeholder = ' --- here ---';
label.appendChild(input);
let button = document.createElement('button');
button.textContent = 'Yoda Say';
body.appendChild(label);
body.appendChild(button);
let p = document.createElement('p');
body.appendChild(p);
button.setAttribute('disabled','disabled');
p.textContent = 'How Yoda says comes here.'

input.oninput = function(){
  if(input.value === ''){
    button.setAttribute('disabled','disabled');
  } else {
    button.removeAttribute('disabled');
  }
};

button.onclick = function(){
  let url = 'https://yoda.p.mashape.com/yoda?sentence=';
  url += input.value.split(' ').join('+');
  let apikey = '5mTSLQJVTDmshrtJtJVNaO80Jn1sp1bLfwvjsn3Apsq52aLvHM';

  let myHttpRequest = new XMLHttpRequest();

  myHttpRequest.onreadystatechange = function(){
    console.log(myHttpRequest);
    if(myHttpRequest.readyState === 4){
      console.log(myHttpRequest.status);
    }
  };

  myHttpRequest.open('get', url, true);
  myHttpRequest.setRequestHeader('X-Mashape-Key', apikey);
  myHttpRequest.setRequestHeader('Accept', 'text/plain');
  myHttpRequest.send();


};



// unirest.get("https://yoda.p.mashape.com/yoda?sentence=You+will+learn+how+to+speak+like+me+someday.++Oh+wait.")
// .header("X-Mashape-Key", "ScT21Cav4cmshA8t6dir5JYl9UVwp1LsnUbjsn5RSZDR3dAKWJ")
// .header("Accept", "text/plain")