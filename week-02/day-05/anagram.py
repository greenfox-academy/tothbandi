# Exercise

# Create a function named is anagram following your current language's style guide. 
# It should take two strings and return a boolean value depending on whether its an anagram or not.


def dict_of_letters(a_str):
    a_dict = {}
    for c in a_str:
        if c not in a_dict:
            a_dict[c]=1
        else:
            a_dict[c] += 1
    return a_dict

def is_anagram(str1, str2):
    print(str1)
    print(str2)
    if dict_of_letters(str1) == dict_of_letters(str2):
        return True
    else:
        return False
    
    # A function with for loop
    #
    # d1 = dict_of_letters(str1)
    # l1 = sorted(d1.keys())
    # d2 = dict_of_letters(str2)
    # l2 = sorted(d2.keys())
    # for i in range(len(l1)):
    #     if l1[i] != l2[i] or d1[l1[i]] != d2[l2[i]]:
    #         return False
    # return True

print(is_anagram("kék", "zöld"))

print(is_anagram("animali", "almaini"))

