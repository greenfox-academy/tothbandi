# Create a method that decrypts reversed-order.txt
def decrypt(file_name):
    try:
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()

        lines.reverse()

        file = open("normal-order.txt", 'a')
        for line in lines:
            file.write(line)
        file.close()
    except:
        print("any problem")

decrypt("reversed-order.txt")

