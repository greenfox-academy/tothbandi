

students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1}
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

def sum_of_candies(students_list):
    candies = 0
    for i in students_list:
        candies += i['candies']
    return candies

def sum_of_certain_age(students_list):
    age = 0
    for i in students_list:
        if i['candies'] < 5:
            age += i['age']
    return age

print(sum_of_candies(students))
print(sum_of_certain_age(students))

