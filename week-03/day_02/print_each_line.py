# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"


def prints_file(file_name, ver = 0):
    try:
        file = open(file_name, 'r')
        if ver == 0:
            for line in file:
                print(line, end='')
            print()
        elif ver == 1:
            lines = file.readlines()
            for line in lines:
                print(line, end='')
            print()
        else:
            print("no such parameter.")
        file.close()

    except FileNotFoundError:
        print("Unable to read file: my-file.txt")

prints_file("my-file.txt")
prints_file("my-file.txt", 1)
prints_file("my-file.txt", 2)
print("print - BEE: ")
prints_file("BEE")




