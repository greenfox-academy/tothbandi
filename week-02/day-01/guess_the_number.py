# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

n = 13
guess = 0
print("Guess a number!")

while guess != n:
    guess = int(input("Your guess: "))
    if guess < n:
        print("The stored number is higher")
    elif guess > n:
        print("The stored number is lower")
    else:
        print("You found the number: 13")