# - Create a function called `factorio`
#   that returns it's input's factorial

a = int(input("Enter an integer: "))

def factorio(n):
    if n < 0:
        print("Too small, must be 0 or greater!")
        return
    elif n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

print(factorio(a))