# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

a = []

for i in range(4):
    b = []
    for j in range(4):
        if i == j:
            b.append(1)
        else:
            b.append(0)
    a.append([])
    a[i] = b
print(a)
for i in range(4):
    for j in range(4):
        print(a[i][j], end='')
    print()


