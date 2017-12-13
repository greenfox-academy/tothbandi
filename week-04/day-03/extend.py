
# Adds a and b, returns as result
def add(a = 0, b = 0):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

# Returns the median value of a list given as param
def median(pool):
    pool = sorted(pool)
    return pool[int((len(pool) - 1) / 2)]

# Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőűöüóí'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    inspected_chars =  ''
    for char in teve:
        if is_vovel(char) and char not in inspected_chars:
            inspected_chars += char
            teve = (char+'v'+char).join(teve.split(char))
    return teve