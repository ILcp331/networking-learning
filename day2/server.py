import socket
import threading

from utils import get_local_ip
from config import PORT

ADDR = (get_local_ip(), PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print(f'[System] Server hosted on {ADDR[0]}:{ADDR[1]}')
