# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

n = int(input("enter a positiv integer :"))

def summa(n):
    if n == 1:
        return 1
    else:
        return n + summa(n-1)

print(summa(n))

