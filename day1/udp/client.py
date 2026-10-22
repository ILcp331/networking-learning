import socket
import datetime


message = f'{datetime.datetime.now()}'

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(message.encode(), ('127.0.0.1', 16303))

data, address = client.recvfrom(1024)
print(data.decode())
