class Person:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return super().__str__()


person = Person("小明")
stu = Student(person.name, 23, "male")

print(stu)
















