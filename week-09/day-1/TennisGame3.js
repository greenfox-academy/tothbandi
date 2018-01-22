'use strict';

let TennisGame3 = function(player1Name, player2Name) {
  this.player1Point = 0;
  this.player2Point = 0;

  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame3.prototype.getScore = function() {
  let score;
  if ((this.player1Point < 4 && this.player2Point < 4) && (this.player1Point + this.player2Point < 6)) {
    let point = ["Love", "Fifteen", "Thirty", "Forty"];
    score = point[this.player1Point];
    return (this.player1Point == this.player2Point) ? score + "-All" : score + "-" + point[this.player2Point];
  } else {
    if (this.player1Point == this.player2Point)
      return "Deuce";
    score = this.player1Point > this.player2Point ? this.player1Name : this.player2Name;
    return ((this.player1Point - this.player2Point) * (this.player1Point - this.player2Point) === 1) ? "Advantage " + score : "Win for " + score;
  }
};

TennisGame3.prototype.wonPoint = function(playerName) {
  if (playerName == "player1")
    this.player1Point += 1;
  else
    this.player2Point += 1;
};

if (typeof window === "undefined") {
  module.exports = TennisGame3;
}