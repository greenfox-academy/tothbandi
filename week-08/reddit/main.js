'use strict';

let redditRequest = new XMLHttpRequest();

redditRequest.open('GET', 'https://time-radish.glitch.me/posts', true);
redditRequest.setRequestHeader('Accept', 'application/json');
redditRequest.send();
redditRequest.onreadystatechange = function(){
  if(redditRequest.readyState === 4){
    console.log(redditRequest);
  }
}