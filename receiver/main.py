#!venv/bin/python

import socket, time
from midi import *

UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))

def clamp(value):
    return min(max(0, int(value)), 127)    

while True:
    try:
        
        data, addr = sock.recvfrom(1024)
        cc, value = eval(data.decode('utf-8'))
        cc = clamp(cc)
        value = clamp(value)

        channel = 1
        midi_out.send_control(channel, cc, value)

    except KeyboardInterrupt:
        exit()
