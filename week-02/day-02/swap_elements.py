
# - Create a variable named `abc`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `abc`

abc = ["first", "second", "third"]

print(abc)

str = abc[0]

abc[0] = abc[2]

abc[2] = str

print(abc)
