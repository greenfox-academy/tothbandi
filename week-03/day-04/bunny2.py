# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def sum_bunny_ears(n):
    ear = 0

    if n % 2 == 0:
        ear = 3
    else:
        ear = 2

    if n==1:
        return 2
    else:
        return ear + sum_bunny_ears(n-1)

print(sum_bunny_ears(1))
print(sum_bunny_ears(2))
print(sum_bunny_ears(3))
print(sum_bunny_ears(4))
print(sum_bunny_ears(5))

