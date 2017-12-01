# Exercise

# Write a function to solve Josephus Problem. 
# The program should ask for a number, 
# this number represents how many people are in the "game". 
# The return value should be the number of the "winning" seat.

a = int(input("Program for solving Josephus problem. Enter a number of people: "))

l = [True for _ in range(a)]

if a == 1:
   sword_man = 0
else: 
    sword_man = 0
    next_left_man = 1
    megvan = False
    while not megvan:
        while not l[next_left_man]:
            if next_left_man < len(l) - 1:
                next_left_man += 1
            else:
                next_left_man = 0
        if sword_man == next_left_man:
            megvan = True
        else:
            l[next_left_man] = False
        while not l[next_left_man]:
            if next_left_man < len(l) - 1:
                next_left_man += 1
            else:
                next_left_man = 0
        sword_man = next_left_man
        if next_left_man < len(l) - 1:
            next_left_man += 1
        else:
            next_left_man = 0
print(sword_man + 1)
