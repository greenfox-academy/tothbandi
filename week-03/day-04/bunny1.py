# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def sum_bunny_ears(n):
    if n==1:
        return 2
    else:
        return 2 + sum_bunny_ears(n-1)

print(sum_bunny_ears(1))
print(sum_bunny_ears(11))
