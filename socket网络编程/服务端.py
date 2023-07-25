import socket

# 创建socket对象
socker_server = socket.socket()

# 绑定IP地址和端口
socker_server.bind(("localhost", 8888))

# 监听端口，listen()方法内接受的是一个整数类型，表示接受的链接数量
socker_server.listen(1)

# 等待客户端链接
# result: tuple = socker_server.accept()  # 这个返回值是一个二元元组，且是一个阻滞的方法，如果没有客户端的链接，会阻滞到这一行
# conn = result[0]  # 客户端与服务端的链接对象
# address = result[1]  # 客户端的地址信息
# 也可以写成下面的形式
conn, address = socker_server.accept()
print(f"接受到了客户端的链接，客户端的信息是{address}")

while True:
    # 接受客户端信息，要使用客户端与服务端的本次链接对象，而非socket_server对象
    # recv接受的是缓冲区的大小，一般给1024即可
    # recv方法的返回值是一个字节数组，也就是bytes对象，而非字符串，可以通过decode方法utf-8编码，将字节转为字符串对象
    data: str = conn.recv(1024).decode("utf-8")
    print(f"客户端发来的消息是：{data}")

    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息：\n").encode("utf-8")  # 可以将字符串编码为字节数组对象
    if msg == "exit":
        # 关闭链接
        conn.close()  # 这个是链接对象的关闭
    else:
        conn.send(msg)
        socker_server.close()  # 这个是客户端的关闭




















