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




### communication


### motors
https://randomnerdtutorials.com/esp32-dc-motor-l298n-motor-driver-control-speed-direction/

https://www.tutorialspoint.com/arduino/arduino_dc_motor.htm

L298N
 0.1uF ceramic capacitor

https://www.adafruit.com/product/1312


https://www.seeedstudio.com/blog/2019/04/01/choosing-the-right-motor-for-your-project-dc-vs-stepper-vs-servo-motors/

https://learn.sparkfun.com/tutorials/basic-servo-control-for-beginners/all



https://learn.adafruit.com/adafruit-8-channel-pwm-or-servo-featherwing


add to inventory:
power supply https://www.adafruit.com/product/276 5V 2A (2000mA)
battery holder https://www.adafruit.com/product/830 (and batteries)





## analog inputs

Note you can only read analog inputs on ADC #2 once WiFi has started as it is shared with the WiFi module. Maybe not the case for V2.

battery read
<!-- float measuredvbat = analogReadMilliVolts(VBATPIN);
measuredvbat *= 2;    // we divided by 2, so multiply back
measuredvbat /= 1000; // convert to volts!
Serial.print("VBat: " ); Serial.println(measuredvbat)
 -->


### problems

ok, so SCL 32 and SDA 14 works fine; 14 and 22 did not. Could be a problem with the board itself. So look out to see if it works on another esp. This is fine for the IMU.

but the next question is can I used the servo wing?



