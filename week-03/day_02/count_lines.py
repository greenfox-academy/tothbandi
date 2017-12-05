# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def count_lines_in(file_name):
    try:
        file = open(file_name, 'r')
        lines = file.readlines()
        return len(lines)
        file.close()

    except FileNotFoundError:
        return 0

print(count_lines_in("my-file.txt"))
print(count_lines_in("nincs ilyen fájl"))