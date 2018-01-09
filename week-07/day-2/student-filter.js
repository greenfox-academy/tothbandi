'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function likesCandy(students){
  let filtered = [];
  students.map(function(student){
    if (student['candies'] > 4){
      filtered.push(student['name']);
    }
  });
  return filtered;
}

console.log(likesCandy(students));

function averageCandies(students){
  let sum = 0;
  students.forEach(function(student){
    sum += student['candies'];
  });
  return sum / students.length;
}

console.log(averageCandies(students));

