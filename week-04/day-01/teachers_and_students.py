class Teacher(object):
    def teach(self, student):
        student.learn()
    def answer(self):
        pass

class Student(object):
    def learn(self):
        pass
    def question(self, teacher):
        teacher.answer()

teacher = Teacher()
teacher.teach(Student())

student = Student()
student.question(teacher)

