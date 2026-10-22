import socket
import datetime


message = f'{datetime.datetime.now()}'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 16303))
client.send(message.encode())

data = client.recv(1024).decode()
print(data)
