'use strict';

const titleInput = document.querySelector('.input-title');
const urlInput = document.querySelector('.input-url');
const submit = document.querySelector('.link-to');
// const server = 'http://secure-reddit.herokuapp.com/simple';
const server = 'https://time-radish.glitch.me';


function sendPost(){
  let title = titleInput.value;
  let url = urlInput.value;
  let sendto = '';
  console.log('clicked');

  let postBody = {};
  postBody.title = title;
  postBody.url = url;
  let redditRequest = new XMLHttpRequest();

  redditRequest.open('POST', `${server}/posts`);
  redditRequest.setRequestHeader('Accept', 'application/json');
  redditRequest.setRequestHeader('Content-Type', 'application/json');


  console.log(postBody);
  redditRequest.send(JSON.stringify(postBody));
  redditRequest.onreadystatechange = function(){
    console.log(redditRequest);
    if(redditRequest.readyState === 4 && redditRequest.status === 200){
        window.location.href = 'index.html';
    }
  }
}

submit.addEventListener('click', function(){
  let title = titleInput.value;
  let url = urlInput.value;
    if(title === '' || url === ''){
      alert('Please fill both fields')
      ;
    } else {
      sendPost();
    }
});
