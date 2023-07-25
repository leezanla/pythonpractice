import threading
import time


def sing():
    while True:
        print("我在唱歌\n")
        time.sleep(1)


def dance():
    while True:
        print("我在跳舞\n")
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()















