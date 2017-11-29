
accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist


# - First task: - Create function that returns the name and balance of cash on an account

def name_and_balance(an_account):
    name = an_account['client_name']
    balance = an_account['balance']
    return name, balance


# - For checking the function

print("Eredeti: ")
for account in accounts:
    print(name_and_balance(account)[0] + " " + str(name_and_balance(account)[1]))
print()


#  - validates the account number

def account_validator(account_number):
    print("validator - vizsgált számla: " + str(account_number))
    for account in accounts:
        print(account['account_number'])
        if account_number == account['account_number']:
            print("A vizsgált számla: ok ")
            return True
    print("A vizsgált számla: nok ")
    return False


# - checkes the account balance
    
def balance_enough(account_number, amount):
    print("balance - vizsgált számla: " + str(account_number) + ", utalandó összeg: " + str(amount))
    for account in accounts:
        if account_number == account['account_number']:
            return amount < account['balance']


# - Second task - Create function that transfers an amount of cash from one account to another

def transfer(from_account_number, to_account_number, amount):
    if account_validator(from_account_number) and account_validator(to_account_number):
        if balance_enough(from_account_number, amount):
            for account in accounts:
                if account['account_number'] == from_account_number:
                    account['balance'] -= amount
                if account['account_number'] == to_account_number:
                    account['balance'] += amount                
        else:
            print("Amount too high")
    else:
        print("404 - account not found")


# - Test cases: 

print("Első számla nem létezik: ")
transfer(1, 43546731, 1)
for account in accounts:
    print(name_and_balance(account)[0] + " " + str(name_and_balance(account)[1]))
print()

print("Második számla nem létezik: ")
transfer(43546731, 1, 1)
for account in accounts:
    print(name_and_balance(account)[0] + " " + str(name_and_balance(account)[1]))
print()

print("Mennyiség túl magas: ")
transfer(11234543, 43546731, 203004199.2)
for account in accounts:
    print(name_and_balance(account)[0] + " " + str(name_and_balance(account)[1]))
print()

print("Minden ok: ")
transfer(11234543, 43546731, 203004000.2)
for account in accounts:
    print(name_and_balance(account)[0] + " " + str(name_and_balance(account)[1]))