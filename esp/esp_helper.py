import esp32, espnow, machine
import network, ubinascii, json
from esp32 import hall_sensor
from machine import ADC, Pin, TouchPad, PWM
from time import sleep, time


# PINS
# https://learn.adafruit.com/adafruit-esp32-feather-v2/pinouts

A0 = ADC(Pin(26), atten=ADC.ATTN_11DB)  # ADC2
A1 = ADC(Pin(25), atten=ADC.ATTN_11DB)  # ADC2
A2 = ADC(Pin(34), atten=ADC.ATTN_11DB)
A3 = ADC(Pin(39), atten=ADC.ATTN_11DB)
A4 = ADC(Pin(36), atten=ADC.ATTN_11DB)
A5 = ADC(Pin(4), atten=ADC.ATTN_11DB)   # ADC2
# A37 = ADC(Pin(37), atten=ADC.ATTN_11DB)

# I/O Pins: 13 (also LED), 12, 27, 33, 15, 32, 14
def IN(pin_n):
    return Pin(pin_n, Pin.IN)

def OUT(pin_n):
    return Pin(pin_n, Pin.OUT)

# use TouchPad(my_pin) to turn into a touch input

# PIX = Pin(0, Pin.OUT)
# can neopixels use the STEMMA connector?
# SW38 = Pin(38, Pin.IN)  # hardware button
# BAT = ADC(Pin(35), atten=ADC.ATTN_11DB)



# P2P NETWORK

def send(message):
    for peer in peers:
        try:
            e.send(peer, message)
        except Exception as exc:
            print("Can't send to", bin_to_hex(peer))

def receive():
    sender, msg = e.recv(0)
    if msg and sender in peers:
        return bin_to_hex(sender), msg.decode()
    else:
        return None, None

def add_peer(hex_mac):
    bin_mac = hex_to_bin(hex_mac)
    e.add_peer(bin_mac)
    peers.append(bin_mac)

def bin_to_hex(bin_mac):
    return ubinascii.hexlify(bin_mac, ':').decode().upper()

def hex_to_bin(hex_mac):
    return ubinascii.unhexlify(hex_mac.replace(':', '').lower())

sta = network.WLAN(network.STA_IF)
sta.active(True)
print("MAC address is", bin_to_hex(sta.config('mac')))
e = espnow.ESPNow()
e.active(True)
peers = []



# IMU

imu = False
calibrated = False
try:
    from bno055_base import BNO055_BASE
    i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(23))
    sleep(.5)
    imu = BNO055_BASE(i2c)
except Exception as exc:
    print(exc)
    
def imu_calibrated():
    global calibrated
    if imu is False:
        print("No IMU")
        return False    
    if not calibrated:
        sys, gyro, accel, mag = imu.cal_status()
        print(f"Calibrating: sys[{sys}] gyro[{gyro}] accel[{accel}] mag[{mag}]")
        #calibrated = imu.calibrated()
        calibrated = gyro + mag == 6 # calibrating accel is onerous and (maybe?) unnecessary
        return False
    return True
    
def get_orientation():
    if imu is False or not calibrated:
        return (0, 0, 0)    
    return imu.euler() # heading, pitch, roll

def get_accel():
    return abs(sum([value for value in imu.lin_acc()]) / 3.0)



# UTIL

class Smoother():

    def __init__(self, factor):
        self.factor = factor
        self.readings = [0] * int(self.factor)
        self.index = 0

    def smooth(self, v):
        self.readings[self.index] = v
        self.index = (self.index + 1) % self.factor
        value = sum(self.readings) / float(self.factor)
        return value








