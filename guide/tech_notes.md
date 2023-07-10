# TECH NOTES


## basic

boot.py is run at boot
main.py is run next, which is the program

https://docs.micropython.org/en/latest/esp32/quickref.html

https://www.coderdojotc.org/micropython/sound/02-play-tone/

https://awesome-micropython.com

I2C: eye-squared-see

Inertial Measurement Unit (IMU)

## p2p

https://randomnerdtutorials.com/esp-now-esp32-arduino-ide/


## IMU

https://stackoverflow.com/questions/64421476/installing-micropython-library-bno055-imu-properly

https://github.com/micropython-IMU/micropython-bno055



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


### motors
https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/

https://www.tutorialspoint.com/arduino/arduino_dc_motor.htm

L298N
 0.1uF ceramic capacitor

https://www.adafruit.com/product/1312


https://www.seeedstudio.com/blog/2019/04/01/choosing-the-right-motor-for-your-project-dc-vs-stepper-vs-servo-motors/

https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/all


## analog inputs

Note you can only read analog inputs on ADC #2 once WiFi has started as it is shared with the WiFi module. Maybe not the case for V2.

battery read
<!-- float measuredvbat = analogReadMilliVolts(VBATPIN);
measuredvbat *= 2;    // we divided by 2, so multiply back
measuredvbat /= 1000; // convert to volts!
Serial.print("VBat: " ); Serial.println(measuredvbat)
 -->


