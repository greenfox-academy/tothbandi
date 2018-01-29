'use strict';

// let counter;
// let arrowUp;
// let arrowDown;

// const server = 'http://secure-reddit.herokuapp.com/simple'; // user
// const server = 'https://time-radish.glitch.me'; // owner
const server = 'http://localhost:3000';

// sendMessage('GET');

getPosts();

function getPosts() {
  let redditRequest = new XMLHttpRequest();
  redditRequest.open('GET', `/posts`, true);
  redditRequest.setRequestHeader('Accept', 'application/json');
  redditRequest.setRequestHeader("Content-Type", "application/json");
  redditRequest.send();
  redditRequest.addEventListener('load', function () {
    let data = JSON.parse(redditRequest.responseText);
    console.log('data = responsetext:\n', data);
    generatePosts(data);
  });
  // redditRequest.onreadystatechange = function(){
  //   if(redditRequest.readyState === redditRequest.DONE){
  //     console.log('request object:\n', redditRequest);
  //     let data = JSON.parse(redditRequest.responseText);
  //     console.log('data = responsetext:\n', data);
  //     generatePosts(data);
  //   } else if(redditRequest.readyState == redditRequest.HEADERS_RECEIVED) {
  //     console.log('response header: \n', redditRequest.getResponseHeader("Content-Type"));
  //   }
  // }
}

function vote(event) {

  let id = event.target.parentElement.dataset.id;
  let direction = event.target.classList[0];
  let redditRequest = new XMLHttpRequest();
  let url = `${server}/posts/${id}/${direction}vote`;
  redditRequest.open('PUT', url);
  redditRequest.setRequestHeader('Accept', 'application/json');
  // redditRequest.setRequestHeader("Content-Type", "application/json");
  redditRequest.send();
  redditRequest.addEventListener('load', () => {
      let data = JSON.parse(redditRequest.responseText);
      event.target.parentElement.childNodes[1].textContent = data[0].score;
  });
  // redditRequest.onreadystatechange = function(){
  //   if(redditRequest.readyState === redditRequest.DONE){
  //     console.log('vote request object:\n', redditRequest);
  //     let data = JSON.parse(redditRequest.responseText);
  //     console.log('data = responsetext:\n', data);
  //     event.target.parentElement.childNodes[1].textContent = data[0].score;
  //   } else if(redditRequest.readyState == redditRequest.HEADERS_RECEIVED) {
  //     console.log('response header: \n', redditRequest.getResponseHeader("Content-Type"));
  //   }
  // }
}


function sendMessage(method, id, direction, event){


  let redditRequest = new XMLHttpRequest();
  
  if(method === 'GET'){
    redditRequest.open('GET', `${server}/posts`);
  } else if(method === 'PUT'){
    let url = `${server}/posts/${id}/${direction}vote`;
    redditRequest.open('PUT', url);
  }
  redditRequest.setRequestHeader('Accept', 'application/json');
  redditRequest.send();
  redditRequest.onreadystatechange = function(){
    if(redditRequest.readyState === 4){
      let data = JSON.parse(redditRequest.responseText);
      console.log(redditRequest);
      if(method === 'GET'){
        generatePosts(data);
      } else if (method === 'PUT'){
        event.target.parentElement.childNodes[1].textContent = data.score;
      }
    }
  }
}

window.addEventListener('click', function(event){
  if(event.target.classList.contains('arrow')){
    vote(event);
  //  let id = event.target.parentElement.dataset.id;
  //  let direction = event.target.classList[0];
  //  sendMessage('PUT', id, direction, event);
  }
});

window.addEventListener('mouseup',function(event){
  event.target.style.backgroundImage = `url("../assets/${event.target.classList[0]}voted.png")`;
});

const toNewPost = document.querySelector('.link-to');
toNewPost.setAttribute('href', 'post.html');

function generatePosts(data){
  console.log(`data:\n ${data}`);
  let posts = document.querySelector('.posts');
  data.forEach(element => {
    posts.appendChild(createPost(element));
  });
}

function createPost(element){
  let post = document.createElement('article');
  post.classList.add('post');
  post.appendChild(createCounter(element.score, element.id));
  post.appendChild(createPostContent(element));
  return post;
} 

function createCounter(score, id){
  let counter = document.createElement('div');
  counter.classList.add('counter');
  counter.setAttribute('data-id', id);
  let arrowUp = document.createElement('button');
  arrowUp.classList.add('up', 'arrow');
  arrowUp.style.backgroundImage = 'url("../assets/upvote.png';
  let likeCounter = document.createElement('p');
  likeCounter.classList.add('like-counter');
  likeCounter.setAttribute('data-like-counter', score);
  likeCounter.textContent = score;
  let arrowDown = document.createElement('button');
  arrowDown.classList.add('down', 'arrow');
  arrowDown.style.backgroundImage = 'url("../assets/downvote.png';
  counter.appendChild(arrowUp);
  counter.appendChild(likeCounter);
  counter.appendChild(arrowDown);
  return counter;
}

function createPostContent(element){
  let href = '';
  if((typeof element.href) === 'undefined'){
    href = element.url;
  } else {
    href = element.href;
  }
  let url = '#';
  let domain = '';
  if(href !== ''){
    let sections = href.split('/');
    while(sections[0] === 'http:' || sections[0] === 'https:' || sections[0] === ''){
      sections.shift();
    }
    let point = sections[0].lastIndexOf('.');
    let end = sections[0].length - 1;
    if(point !== -1 && (point === end - 2 || point === end - 3)){
      url = href;
      domain = sections[0];
    }
  }
  let user = element.user;
  if (typeof user === 'undefined'){
    user = element.owner;
  }
  if (user === '' || user === null){
    user = 'Anonymus';
  }
  let content = document.createElement('div');
  content.classList.add('post-content');
  content.setAttribute('data-id', element.id);
  let title = document.createElement('h2');
  title.classList.add('post-title');
  title.innerHTML = `${element.title} <a href="${url}" class="show-url">(${domain})</a>`;
  content.appendChild(title);
  let submitted = document.createElement('p');
  submitted.classList.add('submitted');
  submitted.innerHTML = 'submitted ' + timeSpend(element.timestamp) + ' by <a href="#" class="user">' + user + '</a>';
  content.appendChild(submitted);
  let links = document.createElement('div');
  links.classList.add('links-in-post');
  let link = document.createElement('a');
  link.classList.add('link-in-post');
  link.setAttribute('href', '#');
  link.textContent = 'modify';
  let link2 = document.createElement('a');
  link2.classList.add('link-in-post');
  link2.setAttribute('href', '#');
  link2.textContent = 'remove';
  links.appendChild(link);
  links.appendChild(link2);
  content.appendChild(links);
  return content;
}

function timeSpend(timestamp){

  if(timestamp < 10000000000){
    timestamp *= 1000;
  }

  timestamp = Date.now() - timestamp;
  timestamp = Math.floor(timestamp / 1000);
  let minutes = Math.floor(timestamp / 60);
  let hours = Math.floor(minutes / 60);
  let days = Math.floor(hours / 24);
  let months = Math.floor(days / 30);
  let years = Math.floor(months / 12);

  if (years > 0){
    return `${years} years ago`;
  } else if (months > 0){
    return `${months} months ago`;
  } else if (days > 0){
    return `${days} days ago`;
  } else if (hours > 0){
    return `${hours} hours ago`;
  } else if (minutes > 0) {
    return `${minutes} minutes ago`;
  } else {
    return 'right now';
  }
}


