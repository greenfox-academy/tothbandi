'use strict';

let test = require('tape');
let tested = require('./anagram');

test('anagram test', function(t){
  t.ok(tested.isAnagram('abca', 'aabc'));
  t.ok(tested.isAnagram('abca', 'aab c'));
  t.ok(tested.isAnagram('abca', 'A bac'));
  t.notOk(tested.isAnagram('apple', 'peach'));
  t.notOk(tested.isAnagram('apple', 'aaple'));
  t.notOk(tested.isAnagram('', 'peach'));
  t.ok(tested.isAnagram('', ''));
  t.end();
});