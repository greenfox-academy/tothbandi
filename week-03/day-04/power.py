# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power(base, exponent):
    if exponent==1:
        return base
    else:
        return base * power(base, exponent-1)

print(power(1,1))
print(power(3,1))
print(power(1,3))
print(power(3,4))
