# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

print("Sum and average of numbers")
a = 0
sum = 0
n = 0
more = True
while more:
    a = int(input("Enter an integer: "))
    sum += a
    n += 1
    more_answer = input("Is there another number? (y/n): ")
    if more_answer == "n":
        more = False
print("Sum: " + str(sum) + ", Average: " + str(sum/n))