# IMUs

An IMU is an "Inertial Measurement Unit"—it's actually three sensors in one, a gyroscope, an accelerometer, and a magnetometer (aka compass). Put together, and with the addition of lots of math (that it does for us), an IMU can tell us how it is oriented in space. 

This comes in the form `heading` (which direction it's pointing relative to the surface of the earth), `pitch` (how much it's angled up or down) and `roll` (how much it's angled side to side). Each of these is a degree value, 0-360.

The IMU we are using is a bno055. Because it's more advanced, unlike other sensors and switches, this one uses a pair of data transfer pins on the ESP32 called SCL and SDA, the last two pins on the top row. To connect it, we use these along with power and ground.

![](img/imu.png)


Before we use the IMU, we have to initialize it in the code, with `start_imu()`. We then check to make sure the IMU is calibrated with `imu_calibrated()`, and while we're waiting, we turn the LED on. Finally, the `get_orientation()` and `get_accel()` functions return data we can use.

`get_orientation()` returns the values described above: `heading`, `pitch`, and `roll`. Use these to control parameters based on the position of the IMU in space.

`get_accel()` returns a single value that is the total acceleration of the unit in all directions. Use this to trigger actions based on movement of the IMU. Note that there will probably be a small value here even if the IMU is at rest.


###### Code

```py
from esp_helper import *

start_imu()

while True:

    if imu_calibrated():
        heading, pitch, roll = get_orientation()
        print(int(pitch), int(roll))
        acceleration = get_accel()
        if acceleration > 5:
            LED.on()  # turn LED on if the sensor is moved
        else:
            LED.off()
    else:
        LED.on()   # indicate whether we still need to calibrate by leaving the LED on
    sleep(.1)
```    

#### Calibration

The three sensors in the IMU have to be calibrated to give accurate readings. When you first start your program, you'll see this in the Thonny console:

```
Calibrating: gyro[3] accel[0] mag[0]
Calibrating: gyro[3] accel[0] mag[0]
Calibrating: gyro[3] accel[0] mag[0]
Calibrating: gyro[3] accel[0] mag[0]
Calibrating: gyro[3] accel[0] mag[0]
Calibrating: gyro[3] accel[0] mag[0]
Calibrating: gyro[3] accel[0] mag[0]
Calibrating: gyro[3] accel[0] mag[1]
Calibrating: gyro[3] accel[0] mag[1]
Calibrating: gyro[3] accel[0] mag[1]
Calibrating: gyro[3] accel[0] mag[1]
Calibrating: gyro[3] accel[0] mag[1]
Calibrating: gyro[3] accel[0] mag[1]
```

`3` means the sensor is calibrated; `0` means it hasn't been yet.

The gyroscope is the easiest to calibrate: letting the IMU be still for a few seconds should be all that it takes. This is simple if your project is sitting on a table, but take note if it's attached to a person or vehicle.

The accelerometer is hard to calibrate. So hard, in fact, that the code in esp_helper will skip it for the time being—the accelerometer also happens to give pretty solid results regardless of whether it's calibrated or not, so it's not worth the headache.

The magnetometer requires movement. So after holding things still for a few seconds to get the gyroscope calibrated, the IMU needs to be moved in a figure-eight motion in the air. This should show a 3 within a few seconds.

`get_orientation()` and `get_accel()` will only return 0s until calibration (of gyro and mag) is complete, so use `imu_calibrated()` to check for that in your code.




<!-- 
Accelerometer Calibration

Place the device in 6 different stable positions for a period of few seconds to allow the accelerometer to calibrate.

Make sure that there is slow movement between 2 stable positions.

The 6 stable positions could be in any direction, but make sure that the device is lying at least once perpendicular to the x, y and z axis.

 -->