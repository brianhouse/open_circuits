import socket

PORT = 5005

def setup():
    global sock
    size(400, 300)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", PORT))

def draw():
    background(255)
    global sock
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print(data, addr)
    ## would be better if this did not block
    # data = float(data.decode('utf-8'))
    # print("received message: %s" % data)
    # print(frameRate)
    # x = map(data, 0.0, 1.0, 0, width)
    # line(x, 0, x, height)
    
    
