my_str = "itheima itcast boxuegu"
print(f"字符串{my_str}中有：{my_str.count('it')}个")
print(f"字符串{my_str}被替换空格后，结果为：{my_str.replace(' ', '|')}")
print(f"字符串{my_str.replace(' ', '|')}，按照|分隔后，得到：{my_str.replace(' ', '|').split('|')}")


