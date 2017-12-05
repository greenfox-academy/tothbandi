# Create a method that decrypts reversed-lines.txt
def decrypt(file_name):
    try:
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()

        for i in range(len(lines)):
            lines[i] = lines[i][::-1]

        file = open("backversed.txt", 'a')
        for line in lines:
            file.write(line)
        file.close()
    except FileNotFoundError:
        print("No file")

decrypt("reversed-lines.txt")
