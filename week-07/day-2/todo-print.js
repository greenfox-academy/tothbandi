'use strict';
// Add "My todo:" to the beginning of the todoText
// Add " - Download games" to the end of the todoText
// Add " - Diablo" to the end of the todoText but with indention

// Expected outpt:

// My todo:
//  - Buy milk
//  - Download games
//      - Diablo

var todoText = " - Buy milk\n";

var todoRows = Array(todoText);

todoRows.unshift('My todo:\n');
todoRows.push(' - Download games\n');
todoRows.push('    ' + ' - Diablo');

todoText = todoRows.join('');

console.log(todoText);