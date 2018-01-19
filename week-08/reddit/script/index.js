'use strict';

let counter;
let arrowUp;
let arrowDown;



let redditRequest = new XMLHttpRequest();
//http://secure-reddit.herokuapp.com/simple
//https://time-radish.glitch.me
redditRequest.open('GET', 'https://time-radish.glitch.me/posts');
redditRequest.setRequestHeader('Accept', 'application/json');
redditRequest.send();
redditRequest.onreadystatechange = function(){
  if(redditRequest.readyState === 4){
    let data = JSON.parse(redditRequest.responseText);
    console.log(data);
    console.log(data.posts[0]);
    generatePosts(data);
    window.addEventListener('click', event => vote(event, data));
  }
};

function vote(event, data){
  // console.log(event.target.classList);
  let id = event.target.parentElement.dataset.id;
  let direction = event.target.classList[0];
  let url = `https://time-radish.glitch.me/posts/${id}/${direction}vote`;
  console.log(url);
  redditRequest.open('PUT', url);
  redditRequest.setRequestHeader('Accept', 'application/json');
  redditRequest.send();
  redditRequest.onreadystatechange = function(){
    console.log(redditRequest);
    if(redditRequest.readyState === 4 && redditRequest.status === 200){
      let data = JSON.parse(redditRequest.responseText);
      console.log('data = ', data);
      console.log(event.target.parentElement.childNodes[1]);
      event.target.parentElement.childNodes[1].textContent = data.score;
      // console.log(data.posts[0]);
    //   generatePosts(data);
    //   window.addEventListener('click', event => vote(event, data));
     }
  };
}


const toNewPost = document.querySelector('.link-to');
toNewPost.setAttribute('href', 'post.html');

function generatePosts(data){
  let posts = document.querySelector('.posts');
  data.posts.forEach(element => {
    posts.appendChild(createPost(element));
  });
}

function createPost(element){
  let post = document.createElement('article');
  post.classList.add('post');
  createCounter(element.score, element.id);
  post.appendChild(counter);
  post.appendChild(createPostContent(element));
  return post;
} 

function createCounter(score, id){
  counter = document.createElement('div');
  counter.classList.add('counter');
  counter.setAttribute('data-id', id);
  arrowUp = document.createElement('button');
  arrowUp.classList.add('up', 'arrow');
  let likeCounter = document.createElement('p');
  likeCounter.classList.add('like-counter');
  likeCounter.setAttribute('data-like-counter', score);
  likeCounter.textContent = score;
  arrowDown = document.createElement('button');
  arrowDown.classList.add('down', 'arrow');
  counter.appendChild(arrowUp);
  counter.appendChild(likeCounter);
  counter.appendChild(arrowDown);
  // return counter;
}

function createPostContent(element){
  let content = document.createElement('div');
  content.classList.add('post-content');
  let title = document.createElement('h2');
  title.classList.add('post-title');
  title.textContent = element.title;
  content.appendChild(title);
  let submitted = document.createElement('p');
  submitted.classList.add('submitted');
  // let timeLeft = document.createElement('span');
  // timeLeft.classList.add('time-left');
  // let testString = timeSpend(element.timestamp);
  // console.log(testString);
  // timeLeft.textContent = testString;
  // let user = document.createElement('a');
  // user.classList.add('user');
  // let testu = textUser(element.user);
  // console.log(testu);
  // user.textContent = testu;

  submitted.innerHTML = 'submitted ' + timeSpend(element.timestamp) + ' by <a href="" class="user">' + textUser(element.user) + '</a>';
  content.appendChild(submitted);
  let links = document.createElement('div');
  links.classList.add('links-to-post');
  let link = document.createElement('a');
  link.classList.add('link-to-post');
  link.textContent = 'modify';
  let link2 = document.createElement('a');
  link2.classList.add('link-to-post');
  link2.textContent = 'remove';
  links.appendChild(link);
  links.appendChild(link2);
  content.appendChild(links);
  return content;
}

function timeSpend(timestamp){
  timestamp -= Date.now();

  let minutes = convert(timestamp, 60);
  let hours = convert(minutes, 60);
  let days = convert(hours, 24);
  let months = convert(days, 30);
  let years = convert(months, 12);

  if (years > 0){
    return years + ' years ago';
  } else if (months > 0){
    return months + ' months ago';
  } else if (days > 0){
    return days + ' days ago';
  } else if (hours > 0){
    return hours + ' hours ago';
  } else if (minutes > 0) {
    return minutes + ' minutes ago';
  } else {
    return 'right now';
  }
}

function convert(time, factor){
  return (time - time % factor) / factor;
}

function textUser(user){
  if (user === null) {
    return 'Anonymus'
  }
  return user;
}

