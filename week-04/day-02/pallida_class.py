class PallidaClass(object):
    def __init__(self, class_name, students = [], mentors = []):
        self.class_name = class_name

    def add_student(self, student):
        self.students.append(student)

    def add_mentor(self, mentor):
        self.mentors.append(mentor)
    
    def info(self):
        print('Pallida {} class has {} students and {} mentors.'.format(
            self.class_name, len(self.students), len(self.mentors)
        ))
