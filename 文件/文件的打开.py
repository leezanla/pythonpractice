count = 0
with open("D:/word.txt", "r", encoding="utf-8") as fp:
    for line in fp:
        for word in line.replace("\n", "").split(" "):
            print(word)
            if word == "itheima":
                count += 1
print(count)
# with open("D:/word.txt", "r", encoding="utf-8") as fp:
#     count = fp.read().count("itheima")
#     print(count)













