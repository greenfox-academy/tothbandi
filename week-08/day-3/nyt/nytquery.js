'use strict';

let url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
url += '?api-key=6bb5e94b1dd24f45a8962bb40df2ac1e&q=the moon landing by Apollo 11';

let myRequest = new XMLHttpRequest();
myRequest.open('GET', url, true);
myRequest.send(null);

console.log(myRequest);

myRequest.onload = function(){
  let myData = JSON.parse(myRequest.responseText);

  let body = document.querySelector('body');

  let ul = document.createElement('ul');

  for(let i = 0; i < 10; i++){
    let article = myData.response.docs[i];
    let li = document.createElement('li');
    let headline = document.createElement('h3');
    let snippet = document.createElement('p');
    let date = document.createElement('p');
    headline.textContent = article.headline.main;
    snippet.textContent = article.snippet;
    date.textContent = article.pub_date.substr(0, 10);
    li.appendChild(headline);
    li.appendChild(snippet);
    li.appendChild(date);
    ul.appendChild(li);
  }

  body.appendChild(ul);

};

