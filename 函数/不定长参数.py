def user_info1(*args):
    print(f"*args的类型是：{type(args)}, 它的内容是：{args}")


def user_info2(**kwargs):
    print(f"**kwargs的类型是：{type(kwargs)}, 它的内容是：{kwargs}")


user_info1(1, 2, "hello")
user_info2(name="小明", age=20)











