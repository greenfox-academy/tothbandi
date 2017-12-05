# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    try:
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()

        for j in range(len(lines)):
            new_line = ""
            for i in range(len(lines[j])):
                if i % 2 == 0:
                    new_line += lines[j][i]
            lines[j] = new_line

        file = open("simplicated.txt", 'a')
        for j in range(len(lines)):
            file.write(lines[j])
        file.close()
    except FileNotFoundError:
        print("No file")


decrypt("duplicated-chars.txt")



        
