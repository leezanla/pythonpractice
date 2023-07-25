# def outer(func):
#     def inner():
#         print("我要睡觉了")
#         func()
#         print("我要起床了")
#     return inner
#
#
# def sleep():
#     import random
#     import time
#     print("睡眠中")
#     time.sleep(random.randint(1, 5))
#
#
# func = outer(sleep)
# func()
def outerr(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我要起床了")
    return inner


@outerr
def sleep():
    import random
    import time
    print("睡眠中")
    time.sleep(random.randint(1, 5))

sleep()














