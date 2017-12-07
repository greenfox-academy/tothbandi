# Given a string, compute recursively a new string where all the 'x' chars have been removed.

string = "This text is still misstyped, but no x in it, and recursion is good"

def str_corrector(string):
    c = string[0]
    if string[0] == 'x':
        c = ''
    if len(string) == 1:
        return c
    else:
        return c + str_corrector(string[1:])

print(str_corrector(string))