# Create a method that find the 5 most common lottery numbers otos.csv

def five_most_frequent(file_name):
    all_numbers = [0] * 90
    with open(file_name) as file:
        for line in file:
            a_line = line.split(";")
            for i in range(-5, 0):
                all_numbers[int(a_line[i]) - 1] += 1
    freq_numbers = {}
    count = 0
    former_max_number = 0
    while count < 5:
        max_pos = 0
        max_number = 0
        for i in range(len(all_numbers)):
            if all_numbers[i] > max_number:
                max_number = all_numbers[i]
                max_pos = i
        if count < 4:
            freq_numbers[max_pos + 1] = all_numbers[max_pos]
            all_numbers[max_pos] *= -1
            former_max_number = max_number
            count += 1
        elif count == 4:
            if max_number == former_max_number:
                freq_numbers[max_pos + 1] = all_numbers[max_pos]
                all_numbers[max_pos] *= -1
            else:
                count += 1
    return freq_numbers

print(five_most_frequent("otos.csv"))
