# Sort that list

# Create a function that takes a list of numbers as parameter
# Returns a list where the elements are sorted in ascending numerical order
# Make a second boolean parameter, if it's true sort that list descending


# Example

# input [34, 12, 24, 9, 5]
# output [5, 9, 12, 24, 34]

input = [34, 12, 24, 9, 5]

def sort_a_list(a_list, order):
    if order == False:
        for i in range(len(a_list)):
            for j in range(i, len(a_list)):
                if a_list[j] < a_list[i]:
                    csere = a_list[j]
                    a_list[j] = a_list[i]
                    a_list[i] = csere
    else:
        for i in range(len(a_list)):
            for j in range(i, len(a_list)):
                if a_list[j] > a_list[i]:
                    csere = a_list[j]
                    a_list[j] = a_list[i]
                    a_list[i] = csere
    return a_list



print(sort_a_list(input, False))
print(sort_a_list(input, True))




