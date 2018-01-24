'use strict';

let test = require('tape');
let tested = require('./apple.js');

test('get apple', function(t){
  t.equal(tested.getApple(), 'peach');
  t.end();
});