# Unique - remove the duplicates

# Create a function that takes a list of numbers as a parameter
# Returns a list of numbers where every number in the list occurs only once


# Example

# input: [1, 11, 34, 11, 52, 61, 1, 34]
# output: [1, 11, 34, 52, 61]

input = [1, 11, 34, 11, 52, 61, 1, 34]
output = []

for input_element in input:
    is_in_the_output = False
    for output_element in output:
        if input_element == output_element:
            is_in_the_output = True
    if not is_in_the_output:
        output.append(input_element)

print(input)
print(output)

