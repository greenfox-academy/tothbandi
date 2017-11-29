# Create a function called 'reverse_string' which takes a string as a parameter
# The function reverses it and returns with the reversed string


reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"

def reverse_string(str):
    return str[::-1]

def reverse_string1(str):
    s = ""
    for i in range(len(str)-1, -1, -1):
        s += str[i]
    return s

def reverse_string2(str):
    s = ""
    for i in range(0, len(str)):
        s += str[len(str) - i - 1]
    return s

print(reverse_string(reversed))
print(reverse_string1(reversed))
print(reverse_string2(reversed))

