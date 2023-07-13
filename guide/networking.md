# Peer-to-Peer Networking

Despite their small size, the ESP32s actually have a wifi antenna, which means they can connect to one another wirelessly. 

To activate it, put `start_wifi()` at the beginning of your code, after the import statement. Then, you'll want to add one or more "peers" using `add_peer()`. These are the other ESP32s to which you want to connect and receive and send messages. ESP32s are identified by what's called the MAC address of their wifi chips. This is a string of text that lists six hexidecimal numbers. 

Once you've done this, every time your program calls `receive()` it will check if a message is waiting, returning the address of the sender along with the message (Python and Micropython are able to return more than one value, which differs from other programming languages). Likewise, you can send a message to all the peers using `send()`.

How do you find the MAC address? When you activate wifi, the ESP32 will print it's own MAC address to the console in Thonny. Copy this value so that you can paste it into the code on another ESP32.

When working with more than one ESP32, when you need to switch from one to another in Thonny, 

close all the files and physically disconnect the previous one from your computer (and power it from a power brick instead). This is the best way to avoid confusion. When working with peer-to-peer networking, make sure that code is running on both ESP32; you may need to hit the reset button.


###### Code

```py
from esp_helper import *

start_wifi()
add_peer("24:6F:28:5F:0C:B8")  # change address for the second ESP32

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

