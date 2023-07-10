# Piezos


###### Code

```py
from esp_helper import *

C = 262
D = 294
E = 330
F = 349
G = 392
A = 440
B = 494
C2 = 523
R = 1

tune = C, D, E, F, G, A, B, C2

beeper = TONE(27)


n = 0
while True:

    beeper.freq(tune[n])
    sleep(.5)    
    n += 1
    if n == len(tune):
        break
    

beeper.freq(R)
beeper.deinit()

```



###### Physical setup