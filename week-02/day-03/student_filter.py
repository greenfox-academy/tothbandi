
students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def more_candies(student_list):
    l = []
    for student in student_list:
        if student['candies'] > 4:
            l.append(student)
    print("Who has got more candies than 4 candies:")
    for student in l:
        print(student['name'])

def average_candies(student_list):
    sum_of_candies = 0
    for student in student_list:
        sum_of_candies += student['candies']
    print(sum_of_candies / len(student_list))

more_candies(students)
average_candies(students)

