# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was
a = int(input("Enter a number: "))

for i in range(a):
    print("%", end="")
print()
if a > 1:
    for j in range(a - 2):
        print("%", end="")
        for i in range(a - 2):
            print(" ", end="")
        print("%")
    for i in range(a):
        print("%", end="")
