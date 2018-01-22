'use strict';

let TennisGame1 = function(player1Name, player2Name) {
  this.m_score1 = 0;
  this.m_score2 = 0;
  this.player1Name = player1Name;
  this.player2Name = player2Name;
};

TennisGame1.prototype.wonPoint = function(playerName) {
  if (playerName === 'player1')
    this.m_score1 += 1;
  else
    this.m_score2 += 1;
};

TennisGame1.prototype.getScore = function() {
  let score = '';
  if (this.m_score1 === this.m_score2) {
    score = this.getScoreEven();
  } else if (this.m_score1 >= 4 || this.m_score2 >= 4) {
    score = this.getScoreOverForty();
  } else {
    score = this.getScoreBelowForty();
  }
  return score;
};

TennisGame1.prototype.getScoreEven = function(){
  let score = '';
  switch (this.m_score1) {
    case 0:
      score = "Love-All";
      break;
    case 1:
      score = "Fifteen-All";
      break;
    case 2:
      score = "Thirty-All";
      break;
    default:
      score = "Deuce";
      break;
  }
}

TennisGame1.prototype.getScoreOverForty = function(){
  let score = '';
  let differenceOfScores = this.m_score1 - this.m_score2;
  if (differenceOfScores === 1) score = "Advantage player1";
  else if (differenceOfScores === -1) score = "Advantage player2";
  else if (differenceOfScores >= 2) score = "Win for player1";
  else score = "Win for player2";
  return score;
}

TennisGame1.prototype.getScoreBelowForty = function(){
  const scoreWords = ['Love', 'Fifteen', 'Thirty', 'Forty'];
  return `${scoreWords[this.m_score1]}-${scoreWords[this.m_score2]}`;
};

if (typeof window === "undefined") {
  module.exports = TennisGame1;
}