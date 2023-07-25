from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:/Environment/Python/python3.9.0/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark")
sc = SparkContext(conf=conf)

# 创建一个rdd对象
rdd = sc.parallelize([1, 2, 3, 4, 5])

# 使用filter方法
rdd2 = rdd.filter(lambda num: num % 2 == 0)

print(rdd2.collect())











