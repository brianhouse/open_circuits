# Neopixels

ALWAYS CONNECT GROUND (–) BEFORE ANYTHING ELSE. Conversely, disconnect ground last when separating.

the idea is to match the power and control voltages


## Single pixels

With through-hole NeoPixels (5mm or 8mm round), add a 0.1 µF capacitor between the + and – pins of EACH PIXEL. Individual pixels may misbehave without this “decoupling cap.” Strips and boards have these caps built-in.


## Short strips

connect the +5V input on the strip to the pad labeled VBAT or BAT on the board, 
-or- just use 3.3v

GND from the strip to any GND pad on the microcontroller board, and DIN to a GPIO 

470ohm resistor on the data line



##### Code

```py
from esp_helper import *

pixels = NEOPIXELS(32, 8)   # create NeoPixel driver on pin 32 for 8 pixels


while True:
    for i in range(15):        
        pixels[i] = choice(((255, 0, 0), (0, 255, 0), (0, 0, 255)))
    pixels.write()              # write data to all pixels
    sleep(.5)


from esp_helper import *

NUM_PIXELS = 60
pixels = NEOPIXELS(NUM_PIXELS)   # create NeoPixel driver on pin 32 for 8 pixels


while True:
    for color in [(255, 0, 0, 0), (0, 255, 0, 0), (0, 0, 255, 0), (0, 0, 0, 255)]:
        for i in range(NUM_PIXELS):
            pixels[i] = color
            pixels.write()
            sleep(.1)

    
```


## Long strips

Separate power supply, 5V DC

Adding a 300 to 500 Ohm resistor between your microcontroller's data pin and the data input on the first NeoPixel can help prevent voltage spikes that might otherwise damage your first pixel. Please add one between your micro and NeoPixels!


On larger projects, you may need to add a capacitor (100 to 1000 µF, 6.3V or higher) across the + and – terminals for more reliable operation. See the photo on the next page for an example.

If powering the pixels with a separate supply, apply power to the pixels before applying power to the microcontroller. Otherwise they’ll try to power “parasitically” through the data line, which could spell trouble for the microcontroller.

If your microcontroller and NeoPixels are powered from two different sources (e.g. separate batteries for each), there must be a ground connection between the two.







https://learn.adafruit.com/adafruit-neopixel-uberguide/powering-neopixels