import socket
import threading

from utils import get_local_ip
from config import PORT, FORMAT, HEADER_SIZE, DISCONNECT_SIGNAL

ADDR = (get_local_ip(), PORT)


def handle_client(conn: socket.socket, addr: socket._RetAddress):
    print(f'[System] New connection from {addr}')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER_SIZE).decode(FORMAT)
        msg_length = int(msg_length)

        msg = conn.recv(msg_length).decode(FORMAT)

        if msg == DISCONNECT_SIGNAL:
            connected = False

        print(f'[{addr}]: {msg}')

    conn.close()


def start_server():
    server.listen()

    print(f'[System] Server started on {ADDR[0]}:{ADDR[1]}')

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f'[System] Active connections: {thread.active_count() - 1}')


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

start_server()
