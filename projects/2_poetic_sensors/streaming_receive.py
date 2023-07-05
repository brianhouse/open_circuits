import socket

PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(data, addr)
    # data = float(data.decode('utf-8'))
    # print("received message: %s" % data)
    # print(frameRate)
    # x = map(data, 0.0, 1.0, 0, width)
    # line(x, 0, x, height)
