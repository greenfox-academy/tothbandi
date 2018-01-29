'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }

  getCircumference() {
    return (this.width + this.height) * 2;
  }
}

let box = new Rectangle(5, 10);

console.log(box.getArea());
console.log(box.getCircumference());