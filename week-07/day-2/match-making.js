'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];


function merge(arr1, arr2){
  if(arr1.length < arr2.length){
    for(let i = 0; i < arr1.length; i++){
      order.push(arr1[i]);
      order.push(arr2[i]);
    }
    for(let i = arr1.length; i < arr2.length; i++){
      order.push(arr2[i]);
    }
  } else {
    for(let i = 0; i < arr2.length; i++){
      order.push(arr1[i]);
      order.push(arr2[i]);
    }
    for(let i = arr2.length; i < arr1.length; i++){
      order.push(arr1[i]);
    }
  }
}

merge(girls, boys);

console.log(order);