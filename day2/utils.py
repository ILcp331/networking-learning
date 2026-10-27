import socket
import requests


def get_public_ip() -> str:
    return requests.get('https://api.ipify.org').text


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception as e:
        print(f'Error getting socket name: {e}')
    finally:
        s.close()
    return ip
