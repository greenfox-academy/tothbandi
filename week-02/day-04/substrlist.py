# Find the substring in the list

# Create a function that takes a string and a list of string as a parameter
# Returns the index of the string in the list where the first string is part of
# Returns -1 if the string is not part any of the strings in the list


# Example

# input: "ching", ["this", "is", "what", "I'm", "searching", "in"]
# output: 4

input = ["this", "is", "what", "I'm", "searching", "in"]
a_string = "ching"

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

def sub_str_in_list(a_list, a_string):
    for i in range(len(a_list)):
        if sub_string(a_list[i], a_string) >= 0:
            return i
    return -1

print(input)
print("ching")
print(sub_str_in_list(input, "ching"))

print(input)
print("not")
print(sub_str_in_list(input, "not"))