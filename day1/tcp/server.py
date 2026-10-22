import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Note: 16303 is just a random number I rolled between 1024~65536 as the port
server.bind(('0.0.0.0', 16303))
server.listen(5)

print(f'Server started, listening at {server.getsockname()}\n')

while True:
    client, address = server.accept()

    message = client.recv(1024).decode()
    print(f'{address}:\n{message}\n')

    client.send('Message received by server.\n'.encode())
