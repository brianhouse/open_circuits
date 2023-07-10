# Networking


###### Code

```py
from esp_helper import *

add_peer("24:6F:28:5F:0C:B8")

i = 0
while True:

    sender, message = receive()
    if message:
        print("Received", message, "from", sender)
        LED.on()
        sleep(1)
        LED.off()
    
    message = str(i)
    print("Sending", message)
    send(message)
    
    i += 1
    i %= 100
    sleep(1)

```

