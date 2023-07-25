class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address) -> None:
        self.name = name
        self.age = age
        self.address = address

    def __lt__(self, other):
        return self.age < other.age


stu1 = Student("小明", 23, "北京")
stu2 = Student("小刚", 25, "南京")
print(stu1 > stu2)

# 输入学生的信息
# for i in range(1, 10 + 1):
#     print(f"当前输入第{i}位学生信息，总共需要录入10位学生信息")
#     name = input("请输入学生姓名：")
#     age = int(input("请输入学生年龄："))
#     address = input("请输入学生地址：")
#     stu = Student(name, age, address)
#     print(f"学生{i}信息录入完成，信息为:【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}】")



















