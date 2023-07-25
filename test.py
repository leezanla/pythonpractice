import random
with open("D:\\file.txt", "w+") as fp:
    for i in range(5000):
        fp.write(str(random.randint(100, 5000)) + "单元" + str(random.randint(500, 8000)) + "室" + "\n")













