# - Create a variable named `aj`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements in `aj`
# - Print the elements of the reversed `aj`

aj = [3, 4, 5, 6, 7]

print(aj)

for i in range(len(aj)//2):
    a = aj[i]
    aj[i] = aj[len(aj) - i - 1]
    aj[len(aj) - i - 1] = a

print("reversed: ")

print(aj)

