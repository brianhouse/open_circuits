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