import winsound


class Student:
    name = None
    age = None

    def say_hi(self):
        winsound.Beep(2000, 3000)
        print(f"Hi 大家好，我是{self.name}")


stu = Student()
stu.say_hi()






















