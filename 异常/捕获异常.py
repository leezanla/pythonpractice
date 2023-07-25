# 基本捕获语法
try:
    f = open("D:/file.txt", "r", encoding="utf-8")
except:
    print("文件不存在")
    f = open("D:/file.txt", "w", encoding="utf-8")
finally:
    f.close()

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    value = 1 / 0
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义或者除以0的错误")

# 捕获全部的异常
try:
    value = 1 / 0
except Exception as e:
    print("出现异常了")











