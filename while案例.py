import random
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(sum)

random_num = random.randint(1, 100)
while True:
    number = int(input("请输入一个数：\n"))
    if random_num > number:
        print("你输入的数值过小\n")
    elif random_num < number:
        print("你输入的数值过大\n")
    else:
        print("恭喜你猜对了\n")
        break


