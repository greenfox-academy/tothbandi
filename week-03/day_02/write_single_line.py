# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

try:
    file = open("my-file2.txt", "w")
    file.write("Bandi T.")
    file.close()
except FileNotFoundError:
    print("Unable to write file: my-file2.txt")