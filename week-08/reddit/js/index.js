'use strict';

let redditRequest = new XMLHttpRequest();

redditRequest.open('GET', 'http://secure-reddit.herokuapp.com/simple/posts', true);
redditRequest.setRequestHeader('Accept', 'application/json');
redditRequest.send();
redditRequest.onreadystatechange = function(){
  if(redditRequest.readyState === 4){
    let data = JSON.parse(redditRequest.responseText);
    console.log(data);
    console.log(data.posts[0]);
    generatePosts(data);
  }
};

const toNewPost = document.querySelector('.link-to-new-post');
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
  post.appendChild(createCounter(element.score));
  post.appendChild(createPostContent(element));
  return post;
} 

function createCounter(score){
  let counter = document.createElement('div');
  counter.classList.add('counter');
  let arrowUp = document.createElement('button');
  arrowUp.classList.add('up', 'arrow');
  let likeCounter = document.createElement('p');
  likeCounter.classList.add('like-counter');
  likeCounter.setAttribute('data-like-counter', score);
  likeCounter.textContent = score;
  let arrowDown = document.createElement('button');
  arrowDown.classList.add('down', 'arrow');
  counter.appendChild(arrowUp);
  counter.appendChild(likeCounter);
  counter.appendChild(arrowDown);
  return counter;
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
  timestamp /= 1000;
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