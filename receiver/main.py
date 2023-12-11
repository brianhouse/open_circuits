#!venv/bin/python

import socket
from midi import *

UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))

while True:
    try:
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8')
        print(f"Received message ({message}) from {addr}")
    except KeyboardInterrupt:
        exit()

