import socket


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Note: 16303 is just a random number I rolled between 1024~65536 as the port
server.bind(('0.0.0.0', 16303))

print(f'Server started, listening at {server.getsockname()}\n')

while True:
    data, address = server.recvfrom(1024)

    message = data.decode()
    print(f'{address}\n{message}\n')

    server.sendto('Message received by server.\n'.encode(), address)
