

class Person:
    possible_sex = {'мужской', 'женский'}

    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        if sex in self.possible_sex:
            self.sex = sex
        else:
            raise NameError('Неверный пол')


class Teacher(Person):
    def __init__(self, name: str, age: int, sex: str):
        super().__init__(name, age, sex)
        self.students_taught: int = 0

    def teach(self, topic: str, *args):
        for pupil in args:
            pupil.take(topic)
            self.students_taught += 1

class Student(Person):
    def __init__(self, name: str, age: int, sex: str):
        super().__init__(name, age, sex)
        self.knowledge = []

    def __len__(self):
        return len(self.knowledge)

    def take(self, topic: str):
        self.knowledge.append(topic)

    def forget(self):
        if self.knowledge:
            self.knowledge.pop(randrange(len(self.knowledge)))

class Materials:
    def __init__(self, *args):
        self.topic = list(args)

    def __len__(self):
        return len(self.topic)
