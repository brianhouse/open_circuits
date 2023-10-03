//

1/8" jacks
we have small amps, can they get smaller?

ie, can we run those 3v speakers from within the box? with a small amp and batteries?
https://www.adafruit.com/product/987
https://www.adafruit.com/product/771 -- 3xAA (also need lots of batteries)
https://www.adafruit.com/product/3692 -- phono jack

so the idea here is we use Tone to drive the phono jack, that gets amplified.

then it's a question of what can be done in software with tone


ok, but conversely, it looks like i2c can be used to hook them up directly, which is better.
https://github.com/miketeachman/micropython-i2s-examples
on the software side, this is writing samples. which I thought python was too slow to do?
but this is programmatically complicated.

https://docs.micropython.org/en/latest/library/machine.I2S.html#machine-i2s


ok, so regardless, this is interesting and should be pursued. maybe PWM for now, and then more later? it's software synthesis on the ESP32, in samples. so essentially Id need to write a small synth library. which would be good for me.

but can PWM just go straight to an amp/speaker? 

this is what I did for Acid Love. so yeah.



//

https://www.coderdojotc.org/micropython/sound/

//

so check this out:

https://www.electro-smith.com/daisy/daisy


this isn't different from an ESP with an audio dac on it. and the code is from various platforms. but it's obviously not micropython.

...but it _is_ Pd. so could totally use that in a music course. design a synth, put it in a box with knobs. basically what Seth is doing.

too much for this course.


[
do I care about this kind of thing in my own practice anymore?
that's the thing -- I'm looking for it to go somewhere. not for the sake of the thing.
]

////


hold the phone, there's wav examples on this: https://github.com/miketeachman/micropython-i2s-examples


so look, the MAX chip is I2S, the TPA is just an amplifier for PWM. that's the default here, but the instrument is just going to be making square waves, which is not so satisfying. 

...but real synthesis is unlikely, right? unless I make a wavetable library.

playing a wave file could work, but requires an SD card reader. exists?

//


ok, so I still have the wrong thing.

we have 4ohm 3W speakers


MAX98357A I2S breakout -- mono, direct to speaker, 3.2W at 4ohms
https://www.adafruit.com/product/3006
https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp
You can provide 2.5V up to 5.5V. Note that at 5V you can end up putting up to 2.8W into your speaker, so make sure your power supply can easily handle up to 650mA and we recommend a power supply spec'd for at least 800mA to give yourself some 'room'
--> so, external power


TPA2012  Stereo 2.1W at 4ohms -- needs external power to VDD and GND, input is an audio signal
https://www.adafruit.com/product/1552
https://learn.adafruit.com/adafruit-ts2012-2-8w-stereo-audio-amplifier/


MAX98306 Stereo 3.7W at 4ohms -- external power, input is an audio signal
https://www.adafruit.com/product/987



so the MAX98306 is useless, the TPA2012 is good if we're going to use TONE with real speakers, and MAX98357A is required for I2S.

except... TPA did less than a piezo when I tried.


/

so these little power supplies are useful.

but could also potentially power off of the BAT pin, no? can batteries handle any amps? I guess it's just a matter of draining.



https://learn.adafruit.com/adafruit-adalogger-featherwing



You know, with an SD card reader and a GPS feather wing (https://learn.adafruit.com/adafruit-ultimate-gps-featherwing), I wonder if I could make a Macrophone logger.

missing the USB though, with power.


what other things can I make?


//

DIN 14
BCLK 32
LRC 15

///

MAX98357A I2S breakout:
LRC (Left/Right Clock) - this is the pin that tells the amplifier when the data is for the left channel and when its for the right channel
BCLK (Bit Clock) - This is the pin that tells the amplifier when to read data on the data pin.
DIN (Data In) - This is the pin that has the actual data coming in, both left and right data are sent on this pin, the LRC pin indicates when left or right is being transmitted
GAIN	Can change gain setting with resistors
SD		Shutdown and channel select                  ---> do I need to connect this or no?
Vin 	Power
GND		Ground

15dB if a 100K resistor is connected between GAIN and GND
12dB if GAIN is connected directly to GND                       <-- do this one
9dB if GAIN is not connected to anything (this is the default)
6dB if GAIN is connected directly to Vin
3dB if a 100K resistor is connected between GAIN and Vin

If SD is connected to ground directly (voltage is under 0.16V) then the amp is shut down
If the voltage on SD is between 0.16V and 0.77V then the output is (Left + Right)/2, that is the stereo average. 
If the voltage on SD is between 0.77V and 1.4V then the output is just the Right channel
If the voltage on SD is higher than 1.4V then the output is the Left channel.

///

From the ESP32
sck_pin   # Serial clock output   ---> BCLK
ws_pin    # Word clock output     ---> LRC ??
sd_pin    # Serial data output    ---> DIN


<!-- https://learn.sparkfun.com/tutorials/i2s-audio-breakout-hookup-guide/all -->