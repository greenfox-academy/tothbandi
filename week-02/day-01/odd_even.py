# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")