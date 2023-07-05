boot.py is run at boot
main.py is run next, which is the program


https://learn.adafruit.com/adafruit-huzzah32-esp32-feather/pinouts

https://docs.micropython.org/en/latest/esp32/quickref.html

https://www.coderdojotc.org/micropython/sound/02-play-tone/

https://awesome-micropython.com

### output futures

outputs
- motor
- neopixels
from neopixel import NeoPixel

what's in-between?
- mapping
- delays
- state machines (nonlinear-narrative)

need an intro of basic electronics info? maybe no.


https://github.com/micropython-IMU/micropython-fusion

https://microcontrollerslab.com/micropython-mpu-6050-esp32-esp8266/

I2C: eye-squared-see

Inertial Measurement Unit (IMU)

### wifi

digitalmediastudio
212212212

check for open ports:
nc -vnzu 10.4.15.228 1-8000


### accels

MPU-6050
accel + gyro (6 degrees)




copy folders

ampy --port /dev/tty.usbserial-01D5EBF4 put uosc

ls /dev/tty.*

p2p
https://randomnerdtutorials.com/esp-now-esp32-arduino-ide/


### neopixels

https://learn.adafruit.com/neopixel-levelshifter
https://learn.adafruit.com/adafruit-neopixel-uberguide/basic-connections

USB pin is 5 volts off a plugged in USB, this also works.
for a short strand (a segment), 3.3v logic is fine, it's just a simple connection with a 470ohm resistor on the data line

so get individual neopixels also!
https://www.adafruit.com/product/1938
https://www.adafruit.com/product/1734

put neopixels into esp_helper so it's like:
pixels = Pixels(S21)
pixels[i] = color


```py
from esp_helper import *
from machine import Pin
from neopixel import NeoPixel
from random import random, choice

pin = Pin(21, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 15)   # create NeoPixel driver on GPIO0 for 8 pixels


while True:
    for i in range(15):        
        np[i] = choice(((255, 0, 0), (0, 255, 0), (0, 0, 255)))
#        np[i] = 0, 0, 255
    np.write()              # write data to all pixels
    #r, g, b = np[0]         # get first pixel colour
    sleep(.1)
```

### communication
https://forums.raspberrypi.com/viewtopic.php?t=300474


### motors
https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/

https://www.tutorialspoint.com/arduino/arduino_dc_motor.htm

L298N
 0.1uF ceramic capacitor

https://www.adafruit.com/product/1312


### oled
https://learn.adafruit.com/monochrome-oled-breakouts

use the featherwing or a more general breakout?
