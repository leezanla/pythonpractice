from pyspark import SparkContext, SparkConf
import json
import os
os.environ["PYSPARK_PYTHON"] = "D:/Environment/Python/python3.9.0/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("spark_test")
sc = SparkContext(conf=conf)

json_str_rdd = sc.textFile("D:/orders.txt").flatMap(lambda x: x.split("|"))

# 转为字典
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))

# 取出城市和销售额数据
city_and_money = dict_rdd.map(lambda x: (x["areaName"], int(x["money"])))  # 千万不要忘记int()

print(city_and_money.collect())
# 取出城市和总的销售额
city_and_all_money = city_and_money.reduceByKey(lambda a, b: a + b)

order_by_money = city_and_all_money.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

# 各个城市的销售额排名

print(order_by_money.collect())












