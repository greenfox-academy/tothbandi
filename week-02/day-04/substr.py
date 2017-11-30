# Find part of an integer

# Create a function that takes two strings as a parameter
# Returns the starting index where the second one is starting in the first one
# Returns -1 if the second string is not in the first one
# Example

# input: "this is what I'm searching in", "searching"
# output: 17

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

print(sub_string("this is what I'm searching in", "searching"))
print(sub_string("this is what I'm searching in", "B searching"))



      