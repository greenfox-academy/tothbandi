# - Create a variable named `am` and assign the value `kuty` to it
# - Write a function called `appendA` that gets a string as an input
#   and appends an 'a' character to its end
# - Print the result of `appendA(am)`

am = "kuty"

def appendA(str):
    return str + "a"

print(appendA(am))


# - Create a variable named `nimals`
#   with the following content: `["kuty", "macsk", "cic"]`
# - Add all elements an `"a"` at the end

nimals = ["kuty", "macsk", "cic"]

print(nimals)

for i in range(len(nimals)):
    nimals[i] = appendA(nimals[i])

print(nimals)

