with open("D:/bill.txt", "r", encoding="utf-8") as fp:
    with open("D:/bill.txt.bak", "w", encoding="utf-8") as f:
        for line in fp:
            if line.replace("\n", "").split(",")[-1] != "测试":
                f.write(line)
            # print(line.split(",")[-1])



















