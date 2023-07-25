with open("D:\\1033-2.txt", "r+", encoding="utf-8") as fp:
    with open("D:\\前缀.txt", "a+", encoding="utf-8") as fp_1:
        with open("D:\\后缀.txt", "a+", encoding="utf-8") as fp_2:
            for line in fp.readlines():
                if "街道" in line:
                    li = line.split("街道")
                    fp_1.write(li[0] + "街道" + "\n")
                    fp_2.write(li[-1])
                elif "乡" in line:
                    li = line.split("乡")
                    fp_1.write(li[0] + "乡" + "\n")
                    fp_2.write(li[-1])
                elif "镇" in line:
                    li = line.split("镇")
                    fp_1.write(li[0] + "镇" + "\n")
                    fp_2.write(li[-1])
                else:
                    fp_1.write(fp.readline())











