for i in range(1, 4):
    number = (int(input("请输入一个数：")))
    if number == 10:
        print(f"恭喜你猜对了\n")
        exit()
    elif number < 10:
        print(f"你猜的数值有点小，还有{3 - i}次机会\n")
    elif number > 10:
        print(f"你猜的数值有点大，还有{3 - i}次机会\n")
    if i == 3:
        print(f"我想结果是：10\n")





