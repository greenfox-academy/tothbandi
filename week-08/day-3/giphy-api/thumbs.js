'use strict';
let body = document.querySelector('body');

let myRequest = new XMLHttpRequest();
myRequest.open('GET', 'https://api.giphy.com/v1/gifs/search?api_key=6Gw14Q2I7Mrn4RXmhDfJx9zujCAO24V8&q=dog&limit=25&offset=0&rating=G&lang=en', true); // Also try http://444.hu/feed
myRequest.send(null);
myRequest.onload = function(){
  let myData = JSON.parse(myRequest.responseText);
  console.log(myData);
  let myThumbs = createThumbs(myData);
  let formerIndex = 0;
  let formerUrl = myData.data[formerIndex].images.fixed_height_small_still.url;
  body.onclick = function(e){
    myThumbs[formerIndex].setAttribute('src', formerUrl);
    
    let index = e.target.getAttribute('data-serno');
    formerIndex = index;    
    formerUrl = myThumbs[formerIndex].getAttribute('src');
    
    let url = myData.data[index].images.original.url;

    myThumbs[index].setAttribute('src', url);

    console.log('dbl cklicked' + e.target.getAttribute('data-serno'));
  }
  // } addEventListener('click', click(myThumbs, myData));
};
myRequest.onreadystatechange = console.log(myRequest.status);

function createThumbs(mydata){
  for(let i = 0; i < 16; i++){
    let img = document.createElement('img');
    let url = mydata.data[i].images.fixed_height_small_still.url;    
    img.setAttribute('src', url);
    img.setAttribute('data-serno', i);
    body.appendChild(img);
  }
  let myThumbs = document.querySelectorAll('img');
  return myThumbs;
};

