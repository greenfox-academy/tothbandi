# Exercise

# Write a program where the program chooses a number between 1 and 100.
# The player is then asked to enter a guess. If the player guesses wrong,
# then the program gives feedback and ask to enter an other guess until 
# the guess is correct.

# Make the range customizable (ask for it before starting the guessing).
# You can add lives. (optional)

import random

a = input("Guess a number quiz. Please enter the bounds: e.g 0 100: ")
l = a.split(" ")
number = random.randrange(int(l[0]), int(l[1]) + 1)
print("I've the number between " + l[0] + " - " + l[1] +". You have 5 lives.")
i = 4
won = False
while i >= 0 and not won:
    guess = int(input("Your guess: "))
    if guess < number:
        print("Too low. You have " + str(i) + " lives left.")
    elif guess > number:
        print("Too high. You have " + str(i) + " lives left.")
    else:
        print("Congratulations. You won!")
        won = True
    i -= 1
if i == -1:
    print("You loose!")
