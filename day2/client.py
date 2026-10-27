import socket

from config import PORT, FORMAT, HEADER_SIZE, DISCONNECT_SIGNAL


SERVER_IP = input('[System] Enter server address:\n>>> ')
ADDR = (SERVER_IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
