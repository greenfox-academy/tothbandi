# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

a = int(input("Enter the 1. integer: "))
b = int(input("Enter the 2. integer: "))
c = int(input("Enter the 3. integer: "))
d = int(input("Enter the 4. integer: "))
e = int(input("Enter the 5. integer: "))

sum = a + b + c + d + e

print("Sum: " + str(sum) + ", Average: " + str(sum / 5))