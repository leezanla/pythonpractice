from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/Environment/Python/python3.9.0/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

sc = SparkContext(conf=conf)
# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])


# 通过map方法将全部数据都乘10
# def func(data: int) -> int:
#     return data * 10


rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)
print(rdd2.collect())












