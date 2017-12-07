# Write a recursive function that takes one parameter: n and counts down from n.

n = int(input("Enter a positiv integer: "))

def count_down(n):
    print(n)
    if n>0:
        n-=1
        count_down(n)

count_down(n)