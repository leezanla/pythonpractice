# t1 = ("黑马程序员", "itheima", "python")
# print(t1.index("python"))
#
# count = t1.count("python")
# print(count)
#
# print(f"t1元组中的总元素有：{len(t1)}")
#
# i = 0
# while i < len(t1):
#     print(t1[i])
#     i += 1
# for i in t1:
#     print(i)

t2 = ("周杰伦", "111", ["football", "music"])
print(f"年龄是：{t2[1]}")
print(f"姓名是：{t2[0]}")
t2[2].remove("football")
print(f"删除学生爱好中的football，结果是：{t2}")
print("增加爱好：coding到爱好list内")
t2[2].append("coding")
print(f"结果是：{t2}")





