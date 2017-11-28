# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

ag = [3, 4, 5, 6, 7]

print(ag)

for i in range(len(ag)):
    ag[i] = ag[i] * 2

print(ag)