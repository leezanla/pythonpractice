from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/Environment/Python/python3.9.0/python.exe"
if __name__ == '__main__':
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
    sc = SparkContext(conf=conf)
    rdd = sc.parallelize(["hello world", "hello python", "pyspark 666"])
    rdd2 = rdd.map(lambda x: x.split(" "))
    print(rdd2.collect())

    rdd3 = rdd.flatMap(lambda x: x.split(" "))
    print(rdd3.collect())







