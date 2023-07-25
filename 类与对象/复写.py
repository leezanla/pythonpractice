# 定义一个父类
from typing import Any


class Phone:
    IMEI = None
    producer = "HM"

    def call_by_5g(self):
        print("使用5G通话")


# 定义一个子类
class MyPhone(Phone):
    producer = "IT"  # 对父类的属性进行重写

    def call_by_5g(self):   # 对父类中的方法进行重写
        # 调用父类的同名成员，有两种方法，第一种：父类名.成员变量
        print(f"父类中的厂商是：{Phone.producer}")
        Phone.call_by_5g(self)
        # 第二种方式：使用super（）调用父类成员
        print(f"父类中的厂商是：{super().producer}")
        super().call_by_5g()
        print("使用6G通话")


my_phone: MyPhone = MyPhone()
my_phone.call_by_5g()







