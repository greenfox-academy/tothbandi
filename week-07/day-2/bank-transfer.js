'use strict';

var accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an amount of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - amount of cash to transfer
//
// Log "404 - account not found" if any of the account numbers don't exist to the console.

function nameAndBalance(accountNumber){
  let account = accounts.find(account => account['account_number'] === accountNumber);
  return [account['client_name'], account['balance']];
}

console.log(nameAndBalance(43546731));

function transfer(from, to, cash){
  let from_account = accounts.find(account => account['account_number'] === from);
  let to_account = accounts.find(account => account['account_number'] === to);
  if(from_account === undefined || to_account === undefined){
    console.log('404 - account not found');
  } else {
    from_account['balance'] -= cash;
    to_account['balance'] += cash;
  }
}

transfer(11234543,23456311,203004099.2);

console.log(accounts);