# Exercise

# Create a function named create palindrome following your current language's style guide.
# It should take a string, create a palindrome from it and then return it.

def create_palindrome(a_str):
    char_list = []
    for c in a_str:
        char_list.append(c)
    for i in range(len(char_list)):
        a_str=a_str + char_list[len(char_list)-i-1]
    return a_str

print(create_palindrome(""))
print(create_palindrome("greenfox"))
print(create_palindrome("123"))