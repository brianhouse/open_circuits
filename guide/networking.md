# Networking

```py
from esp_helper import *

i = 0
while True:
    host, message = receive()
    if message:
        print("Received", message)
    send(str(i))    
    i += 1
    i %= 100
    sleep(.1)

```
