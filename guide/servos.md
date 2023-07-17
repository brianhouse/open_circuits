# Servos

A servomechanism is a little motor with a built-in sensor that can (reasonably) accurately rotate its arm to a specific position. It's the fundamental means of performing physical actions with microcontrollers, whether that's opening a container or flapping some wings. Additionally, there are "continuous rotation servos" which are just motors that can be turned at a specific speed.

To use servos with the ESP32, we need to use a second circuit board that stacks on top of it. This second board includes a PCA9685 chip, which controls the servos, and an interface so the ESP32 and PCA9685 can talk to each other. It also has various headers to attach and power the servos. This board plugs right into the top of the ESP32.

The ESP32 does not have enough power to run servos itself, so we'll also need an external power supply, which can either be a 5v wall wart or a 4x AA battery pack. The leads from the power go into a small terminal on top of the servo board—use a small screwdriver to open and close the ports, **but be careful not to overtighten**.

Servos have three wires coming out; black/brown is ground, red/orange is power, and white/yellow is "PWM", so be sure to plug them in the right way on your board. There's a small number next to each slot—make note of where you plug your servo in.


![](img/servo.png)


Before we use the servo, we have to initialize it in the code, with `start_servos()`. We then initialize each servo we're going to use with the `Servo()` function, passing in the port number.

Standard servos can rotate 180 degrees. In our code, we use the `.position()` method to set the position to what we want.


###### Code






https://learn.adafruit.com/adafruit-8-channel-pwm-or-servo-featherwing

https://learn.adafruit.com/micropython-hardware-pca9685-pwm-and-servo-driver/micropython

brown is ground
orange is power
yellow is PWM 

Errno 19 ENODEV means that the module couldn't find the I2C sensor


0.19sec/deg (4.8v) 0.15sec/deg (6.0v)

