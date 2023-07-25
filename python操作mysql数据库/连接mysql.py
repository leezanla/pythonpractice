from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="rotqiujc",
)

print(conn.get_server_info())
# 获取到游标对象
cursor = conn.cursor()
conn.select_db("test")
# # 使用游标对象，执行sql语句
# cursor.execute("create table test_pymysql(id int, info varchar(255));")
# 执行插入数据
cursor.execute("insert into student(id, name, age) values ('4', '小刚', '26')")
conn.commit()
# 关闭数据库的链接
conn.close()















