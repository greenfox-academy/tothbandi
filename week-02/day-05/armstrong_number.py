# Exercise

# Write a simple program to check if a given number is an armstrong number. 
# The program should ask for a number. 
# E.g. if we type 371, the program should print out: The 371 is an Armstrong number.

print("Inspect if a given number is an Armstrong number.")
a = input("Please enter a number: ")

exponent = len(a)

arm_sum = 0
for c in a:
    arm_sum += int(c)**exponent

if arm_sum == int(a):
    print("Hurray, " + a + " is an Armstrong number!")
else:
    print("Pity, " + a + " is not an Armstrong number!")
    

