# Exercise

# Create a function named search palindrome following your current language's style guide.
# It should take a string, search for palindromes that at least 3 characters 
# long and return a list with the found palindromes.


# A megtalált palindromot teljes szélességre keterjeszti, majd a 
# palindrom közepe felé haladva a listába rakja az egyre kisebb részeket
# és visszaadja a listát

def palindrom_to_list(a_str, before, after, a_list):
    while a_str[before] == a_str[after] and before > 0 and after < len(a_str) - 1:
        before -= 1     
        after += 1

    if a_str[before] != a_str[after]:
        before += 1    
        after -= 1

    while before + 2 <= after:        
        if after == len(a_str)-1:    
            a_list.append(a_str[before:])
        else:    
            a_list.append(a_str[before:after + 1])    
        before += 1
        after -= 1

    return a_list

def search_palindrome(a_str):
    a_list = []
    if len(a_str) >= 3:
        before = 0      # 3 karakter széles ablakot vizsgál
        after = 2
        while True:
            if a_str[before] == a_str[after]:
                palindrom_to_list(a_str, before, after, a_list)
            
            if after == len(a_str) - 1: # ha végigért a sztringen kilép
                return a_list
            else:           # ha nem, az ablakot eggyel növeli, és 4 széles ablakkal
                after += 1  # hasonló módon vizsgál
                            
            if a_str[before] == a_str[after] and a_str[before+1] == a_str[after-1]:
                palindrom_to_list(a_str, before, after, a_list)
    
            before += 1  # ablak bal szélét növeli, ezzel előáll a következő 3 széles ablak              
    return a_list

print(search_palindrome("dog goat dad duck doodle never"))
print(search_palindrome("apple"))
print(search_palindrome("racecar"))
print(search_palindrome("dad"))

