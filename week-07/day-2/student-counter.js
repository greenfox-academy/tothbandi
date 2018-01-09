'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs: 
// - how many candies are owned by students

// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies

function sumOfCandies(students){
  let candies = 0;
  students.forEach(student => candies += student['candies']);
  return candies;
}

function ages(students){
  let age = 0;
  students.forEach(function(student){
    if(student['candies'] < 5){
      age += student['age']; 
    }
  });
  return age;
}

console.log(sumOfCandies(students));
console.log(ages(students));
