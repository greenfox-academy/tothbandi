# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

string = "This teyt is still misstyped, but recursion is good"

def str_corrector(string):
    c = string[0]
    if string[0] == 'y':
        c = 'x'
    if len(string) == 1:
        return c
    else:
        return c + str_corrector(string[1:])

print(str_corrector(string))