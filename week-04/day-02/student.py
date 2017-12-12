from person import Person

class Student(Person):
    def __init__(self, name, age, gender, previous_organization = 'The School of Life', skipped_days = 0):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print('Be a junior software developer.')

    def introduce(self):
        print('Hi, I`m {}, a(n) {} year old {} from {} who skipped {} days from the course already.'.format(
            self.name, self.age, self.gender, self.previous_organization, self.skipped_days
        )) 

    def skip_days(self, number_of_days):
        self.number_of_days += number_of_days
    
