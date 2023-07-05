#!/usr/bin/env python3

import serial
from time import sleep
from datetime import datetime, timedelta

try:
    with serial.Serial('/dev/tty.usbserial-0264F709',
                        baudrate = 115200,
                        stopbits = serial.STOPBITS_ONE,
                        bytesize = serial.EIGHTBITS,
                        writeTimeout = 0,
                        timeout = 10,
                        rtscts = False,
                        dsrdtr = False) as esp:

        while True:
            esp.write(b'a')
            result = esp.readline().decode('utf-8').strip()
            try:
                result = float(result)
            except:
                pass
            print(result)

except serial.SerialException as e:
    print(e)
