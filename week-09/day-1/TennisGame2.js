'use strict';

let TennisGame2 = function(player1Name, player2Name) {
  this.Player1point = 0;
  this.Player2point = 0;

  this.Player1result = "";
  this.Player2result = "";

  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame2.prototype.getScore = function() {
  let score = "";

  if (this.Player1point === this.Player2point && this.Player1point < 3) {
    if (this.Player1point === 0)
        score = "Love";
    if (this.Player1point === 1)
        score = "Fifteen";
    if (this.Player1point === 2)
        score = "Thirty";
    score += "-All";
  }

  if (this.Player1point === this.Player2point && this.Player1point > 2){
      score = "Deuce";
  }

  if (this.Player1point > 0 && this.Player2point === 0) {
    if (this.Player1point === 1)
      this.Player1result = "Fifteen";
    if (this.Player1point === 2)
      this.Player1result = "Thirty";
    if (this.Player1point === 3)
      this.Player1result = "Forty";

    this.Player2result = "Love";
    score = this.Player1result + "-" + this.Player2result;
  }
  if (this.Player2point > 0 && this.Player1point === 0) {
    if (this.Player2point === 1)
      this.Player2result = "Fifteen";
    if (this.Player2point === 2)
      this.Player2result = "Thirty";
    if (this.Player2point === 3)
      this.Player2result = "Forty";

    this.Player1result = "Love";
    score = this.Player1result + "-" + this.Player2result;
  }

  if (this.Player1point > this.Player2point && this.Player1point < 4) {
    if (this.Player1point === 2)
      this.Player1result = "Thirty";
    if (this.Player1point === 3)
      this.Player1result = "Forty";
    if (this.Player2point === 1)
      this.Player2result = "Fifteen";
    if (this.Player2point === 2)
      this.Player2result = "Thirty";
    score = this.Player1result + "-" + this.Player2result;
  }
  if (this.Player2point > this.Player1point && this.Player2point < 4) {
    if (this.Player2point === 2)
      this.Player2result = "Thirty";
    if (this.Player2point === 3)
      this.Player2result = "Forty";
    if (this.Player1point === 1)
      this.Player1result = "Fifteen";
    if (this.Player1point === 2)
      this.Player1result = "Thirty";
    score = this.Player1result + "-" + this.Player2result;
  }

  if (this.Player1point > this.Player2point && this.Player2point >= 3) {
    score = "Advantage player1";
  }

  if (this.Player2point > this.Player1point && this.Player1point >= 3) {
    score = "Advantage player2";
  }

  if (this.Player1point >= 4 && this.Player2point >= 0 && (this.Player1point - this.Player2point) >= 2) {
    score = "Win for player1";
  }
  if (this.Player2point >= 4 && this.Player1point >= 0 && (this.Player2point - this.Player1point) >= 2) {
    score = "Win for player2";
  }
  return score;
};

TennisGame2.prototype.SetPlayer1Score = function(number) {
  for (let i = 0; i < number; i++) {
    this.Player1Score();
  }
};

TennisGame2.prototype.SetPlayer2Score = function(number) {
  for (let i = 0; i < number; i++) {
    this.Player2Score();
  }
};

TennisGame2.prototype.Player1Score = function() {
  this.Player1point++;
};

TennisGame2.prototype.Player2Score = function() {
  this.Player2point++;
};

TennisGame2.prototype.wonPoint = function(player) {
  if (player === "player1")
    this.Player1Score();
  else
    this.Player2Score();
};

if (typeof window === "undefined") {
  module.exports = TennisGame2;
}