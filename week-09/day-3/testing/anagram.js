'use strict';

function getLetters(str){
  let letters = str.split('');
  let countOfLetters = letters.reduce(function (countedLetters, letter) { 
    if (letter !== ' '){
      if (letter in countedLetters) {
        countedLetters[letter]++;
      }
      else {
        countedLetters[letter] = 1;
      }
    }
    return countedLetters;
  }, {});
  return countOfLetters;
}

function isEqualLetters(ltr1, ltr2){
  let letters1 = Object.keys(ltr1);
  let letters2 = Object.keys(ltr2);
  if(letters1.length !== letters2.length){
    return false;
  } else {
    return letters1.every(letter => {
      return letters2.includes(letter) && ltr1[letter] === ltr2[letter];
    });
  }
}

function isAnagram(str1, str2){
  let letters1 = getLetters(str1.toLowerCase());
  let letters2 = getLetters(str2.toLowerCase());
  return isEqualLetters(letters1, letters2);
}

module.exports = {
  'isAnagram': isAnagram
}
