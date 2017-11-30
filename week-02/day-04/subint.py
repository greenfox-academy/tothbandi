# Find the part of int

# Create a function that takes a number and a list of numbers as a parameter
# Returns the indeces of the numbers in the list where the first number is part of
# Returns an empty list if the number is not part any of the numbers in the list


# Example

# input: [1, 11, 34, 52, 61], 1
# output: [0, 1, 4]

input = [1, 11, 34, 52, 61]

def sub_string(string_for_testing, searched_string):
    i = 0
    while i < len(string_for_testing) - len(searched_string) + 1:     
        j = 0
        tested_index = i
        while string_for_testing[tested_index] == searched_string[j]:
            tested_index += 1
            j += 1
            if j == len(searched_string):
                return i
        i += 1
    return -1

def sub_int(a_list, number):
    output = []
    for i in range(len(a_list)):
        if sub_string(str(a_list[i]), str(number)) >= 0:
            output.append(i)
    return output

print(input)
print(1)
print(sub_int(input, 1))

print(input)
print(7)
print(sub_int(input, 7))

