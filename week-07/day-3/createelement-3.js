'use strict';

  const planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]

// Remove the king from the list.
// Fill the list based on the following list of objects.
// Only add the asteroids to the list.
// Each list item should have its category as a class and its content as text content. -->

let asteroids = document.querySelector('.asteroids');
asteroids.removeChild(document.querySelector('.asteroids li'));
planetData.forEach(function(item){
  if(item.asteroid){
    let listItem = document.createElement('li');
    listItem.setAttribute('class', item.category);
    listItem.textContent = item.content;
    asteroids.appendChild(listItem);
  }
});