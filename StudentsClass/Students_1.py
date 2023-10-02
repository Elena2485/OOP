from random import randint, sample, randrange

class Materials:

    def __init__(self, *args):
        self.topics = list(args)

class Student:
    def __init__(self):
        self.knowledge = []

    def tk(self, topic: str):
        self.knowledge.append(topic)

class Teacher:
    students_taught: int = 0
    def teach(self, topic: str, *args):
        for st in args:
            st.tk(topic)
            self.students_taught =+ 1


themes = Materials('Python', 'Version Control Systems', 'Relational Databases' , 'NoSQL databases', 'Message Brokers')

teacher = Teacher()
students = [Student() for _ in range(4)] #функция создания списка

for theme in themes.topics:
    students_set = sample(students, k=randint(1, len(students)))
    teacher.teach(theme, students_set)

for student in students:
    print(student.knowledge)

## Доработайте задачу 2