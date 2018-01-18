'use strict';
let body = document.querySelector('body');
// let form = document.createElement('form');
// form.method = 'POST';
let label = document.createElement('label');
let input = document.createElement('input');
input.type = 'text';
input.placeholder = 'input a city';
input.textContent = '';
label.textContent = 'City: ';
label.appendChild(input);
let button = document.createElement('button');
// button.type = 'submit';
button.textContent = 'Submit';
body.appendChild(label);
body.appendChild(button);
// body.appendChild(form);
button.setAttribute('disabled', 'disabled');
let url = 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=';

button.onclick = function(e){
  console.log(input.value);

  url += input.value;
  console.log(url);
  let myRequest = new XMLHttpRequest();

  myRequest.open('GET',url,true);
  console.log(myRequest.readyState);
  myRequest.setRequestHeader("X-Mashape-Key", "inCAzy7FALmshtuNU549foZvTxK8p1WIeIOjsnyjeNdcRbdmJL")
  myRequest.setRequestHeader("Accept", "application/json");  
  console.log(myRequest.readyState);
  myRequest.send();
  console.log(myRequest.readyState);
  console.log(myRequest);
  console.log(myRequest.status);
}

input.oninput = function(e){
  if(input.value === ''){
    button.setAttribute('disabled', 'disabled');
  } else {
    button.removeAttribute('disabled');
  }
}


  // myRequest.open('GET',url,true);
  // console.log(myRequest.readyState);

//   // http.open('GET', link, true);
//   myRequest.setRequestHeader("X-Mashape-Key", "ScT21Cav4cmshA8t6dir5JYl9UVwp1LsnUbjsn5RSZDR3dAKWJ")
//   myRequest.setRequestHeader("Accept", "application/json");
//   console.log(myRequest.readyState);

//   myRequest.send(null);
//   console.log(myRequest.readyState);
//   if(myRequest.readyState === 'DONE'){
//     let myData = JSON.parse(myRequest.responseText);
//     printout(myData);
//   };

// };

// function printout(data){
//   console.log(data);
// }

// get("https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=New+York")
// .header("X-Mashape-Key", "ScT21Cav4cmshA8t6dir5JYl9UVwp1LsnUbjsn5RSZDR3dAKWJ")
// .header("Accept", "application/json")


