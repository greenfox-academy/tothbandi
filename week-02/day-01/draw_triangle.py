# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

a = int(input("Enter a number: "))
for i in range(a):
    for j in range(i + 1):
        print("*", end="")
    print()