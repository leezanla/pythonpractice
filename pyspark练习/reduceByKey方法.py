from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:/Environment/Python/python3.9.0/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 准备一个RDD
rdd = sc.parallelize([("男", 99), ("男", 68), ("女", 78), ("女", 78)])
# 求男生与女生两个组之和
rdd2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())




