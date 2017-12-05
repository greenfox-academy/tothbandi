# Create a method that decrypts encoded-lines.txt
def decrypt(file_name):
    # try:
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()

        file = open("decoded-lines.txt", 'a')
        for line in lines:
            a_line = ""
            for i in range(len(line)-1):
                if line[i] == " ":
                    a_line += " "
                else:
                    a_line += chr(ord(line[i]) - 1)
            a_line += '\n'
            file.write(a_line)
        file.close()
    # except:
        # print("there is a problem")

decrypt("encoded-lines.txt")



