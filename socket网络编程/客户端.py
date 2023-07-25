# 客户端的开发
import socket

# 创建socket对象
socket_client = socket.socket()

# 连接到服务端
socket_client.connect(("localhost", 8888))

while True:
    msg = input("请输入要与服务端发送的消息：\n")
    if msg == "exit":
        break
    # 发送消息
    socket_client.send(msg.encode("utf-8"))

    # 接收返回的消息
    recv_data = socket_client.recv(1024).decode("utf-8")  # 1024是缓冲区的大小，一般1024即可，同样recv也是阻塞的
    print(f"服务端回复的消息是：{recv_data}")
# 关闭连接
socket_client.close()




















