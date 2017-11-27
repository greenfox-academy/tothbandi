# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was
a = int(input("Enter a number: "))

if a < 4:
    print("Too small!")
else:
    for i in range(a):
        print("%", end="")
    print()
    for j in range(a - 2):
        print("%", end="")
        for i in range(j):
            print(" ", end="")
        print("%", end="")
        for i in range(a - 2 - j - 1):
            print(" ", end="")
        print("%")
    for i in range(a):
        print("%", end="")