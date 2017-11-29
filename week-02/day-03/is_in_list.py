
# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def is_in_list(alist):
    list_of_elements = [4, 8, 12, 15]
    for i in list_of_elements:
        if not i in alist:
            return False
    return True

print(is_in_list(list_of_numbers))