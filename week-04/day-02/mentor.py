from person import Person

class Mentor(Person):
    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', level = 'intermediate'):
        super().__init__(name, age, gender)
        self.level = level

    def get_goal(self):
        print('Educate brilliant junior software developers.')

    def introduce(self):
        print('Hi, I`m {}, a(n) {} year old {} {} level mentor.'.format(
            self.name, self.age, self.gender, self.level
        ))         


