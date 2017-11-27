# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

a = int(input("Enter a number: "))
for i in range(1, a + 1):
    for j in range(a - i):
        print(" ", end="")
    for j in range(i * 2 -1):
        print("*", end="")
    print()
for i in range(1, a):
    for j in range(i):
        print(" ", end="")
    for j in range((a - i) * 2 -1):
        print("*", end="")
    print()