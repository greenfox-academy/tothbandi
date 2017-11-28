# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum(1, 2, 3))