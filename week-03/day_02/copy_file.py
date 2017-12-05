# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(in_file_name, out_file_name):
    try:
        in_file = open(in_file_name, 'r')
        out_file = open(out_file_name, 'w')
        out_file.write(in_file.read())
        out_file.close()
        in_file.close()
        return True
    except:
        return False

print(copy_file("my-file3.txt", "my-file4.txt"))

