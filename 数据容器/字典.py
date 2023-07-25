# 定义一个字典
my_dict = {"王力鸿": 99, "周杰伦": 90, "林俊杰": 77}

# 新增一个元素
my_dict["张学油"] = 100
print(f"新增的字典为：{my_dict}")

# 更新字典中的一个元素
my_dict["周杰伦"] = 50  # 更新与新增的语法是一样的
print(f"更新之后的字典为：{my_dict}")

# 删除一个元素
score = my_dict.pop("周杰伦")
print(f"删除之后的字典为：{my_dict}, 删除元素的值为：{score}")

# 清空元素
# my_dict.clear()
# print(f"清空之后的字典为：{my_dict}")

# 获取全部的key
my_dict_keys = my_dict.keys()
print(f"字典中全部的key为：{my_dict_keys}")

# 统计字典内的元素数量
print(f"字典中的全部元素为：{len(my_dict)}")








