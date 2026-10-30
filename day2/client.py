import socket

from config import PORT, FORMAT, HEADER_SIZE, DISCONNECT_SIGNAL


SERVER_IP = input('[System] Enter server address:\n>>> ')
ADDR = (SERVER_IP, PORT)


def send(message: str):
    msg = message.encode(FORMAT)
    msg_length = len(msg)
    msg_length_send = str(msg_length).encode(FORMAT)

    if len(msg_length_send) > HEADER_SIZE:
        raise ValueError(f'Message too long!')

    msg_length_send += b'\0' * (HEADER_SIZE - len(msg_length_send))

    client.send(msg_length_send)
    client.send(msg)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print(f'\n[System] Successfully connected to {ADDR[0]}:{ADDR[1]}.')
print('Submit a blank message or "!q" to disconnect.')

while True:
    print('\nEnter your message:')
    message = input('>>> ')

    if not message:
        break

    send(message)

send(DISCONNECT_SIGNAL)

print(f'\n[System] Disconnected from {ADDR[0]}:{ADDR[1]}.')
