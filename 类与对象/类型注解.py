# 基础数据类型注解
import json
import random

var_1: int = 10
var_2: str = "hello"
var_3: bool = True
var_4: dict[str, str] = {"name": "alax"}


# 类对象类型注解
class Student:
    pass
student: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"name", "小张"}

# 容器类型详细注解
my_list1: list[int] = [1, 2, 3]
my_tuple1: tuple[int, int, int] = (1, 2, 3)
my_dict1: dict[str, str] = {"name", "小张"}

# 在注释中进行类型注解
var_5 = random.randint(1, 10)  # type: int
var_6 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]
def func():
    return 10
var_7 = func()  # type: int


















