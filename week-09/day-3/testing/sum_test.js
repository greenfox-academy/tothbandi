'use strict';

let test = require('tape');
let tested = require('./sum.js');

test('sum test', function(t){
  t.throws(tested.sum.bind(this, []), Error);
  t.equal(tested.sum([1]), 1);
  t.equal(tested.sum([1,1]), 2);
  t.throws(tested.sum.bind(null), Error);
  t.throws(tested.sum.bind('alma'), Error);
  t.end();
});