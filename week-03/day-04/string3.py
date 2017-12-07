# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

string = "This text is with stars separated"

def str_corrector(string):
    c = string[0]
    if len(string) == 1:
        return c
    else:
        return c + '*' + str_corrector(string[1:])

print(str_corrector(string))