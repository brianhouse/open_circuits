import esp32, espnow, machine
import network, ubinascii, json, random
from esp32 import hall_sensor
from machine import ADC, Pin, TouchPad, PWM
from neopixel import NeoPixel
from time import sleep, time
from random import choice
from random import random as rand


# PINS
# https://learn.adafruit.com/adafruit-esp32-feather-v2/pinouts

#A0 = ADC(Pin(26), atten=ADC.ATTN_11DB)  # ADC2
#A1 = ADC(Pin(25), atten=ADC.ATTN_11DB)  # ADC2
A2 = ADC(Pin(34), atten=ADC.ATTN_11DB)
A3 = ADC(Pin(39), atten=ADC.ATTN_11DB)
A4 = ADC(Pin(36), atten=ADC.ATTN_11DB)
#A5 = ADC(Pin(4), atten=ADC.ATTN_11DB)   # ADC2
A37 = ADC(Pin(37), atten=ADC.ATTN_11DB)

# I/O Pins: 13 (also LED), 12, 27, 33, 15, 32, 14
def IN(pin_n):
    return Pin(pin_n, Pin.IN)

def OUT(pin_n):
    return Pin(pin_n, Pin.OUT)

def TOUCH(pin_n):
    return TouchPad(Pin(pin_n))

def TONE(pin_n):
    return PWM(OUT(pin_n))

def NEOPIXELS(pin_n=32, num=20, bpp=4):
    return NeoPixel(OUT(pin_n), num, bpp)


SCL = 22 # orig esp32 is 22, v2 is 20, but micropython cant use 20
SDA = 23 # orig esp32 is 23
LED = OUT(13)
# PIX = Pin(0, Pin.OUT)     # V2
# BTN = Pin(38, Pin.IN)  # hardware button, V2
# BAT = ADC(Pin(35), atten=ADC.ATTN_11DB)


# P2P NETWORK
peers = []

def start_wifi():
    global e
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    print("MAC address is", bin_to_hex(sta.config('mac')))
    e = espnow.ESPNow()
    e.active(True)

def send(message):
    try:
        for peer in peers:
            try:
                e.send(peer, message)
            except Exception as exc:
                print("Can't send to", bin_to_hex(peer))
    except NameError:
        raise Exception("Wifi not started")

def receive():
    try:
        sender, msg = e.recv(0)
        if msg and sender in peers:
            return bin_to_hex(sender), msg.decode()
        else:
            return None, None
    except NameError:
        raise Exception("Wifi not started")

def add_peer(hex_mac):
    try:
        bin_mac = hex_to_bin(hex_mac)
        e.add_peer(bin_mac)
        peers.append(bin_mac)
    except NameError:
        raise Exception("Wifi not started")        

def bin_to_hex(bin_mac):
    return ubinascii.hexlify(bin_mac, ':').decode().upper()

def hex_to_bin(hex_mac):
    return ubinascii.unhexlify(hex_mac.replace(':', '').lower())


# IMU

def start_imu():
    import imu as imu_module
    global imu, calibrated
    imu = False
    calibrated = False
    i2c = machine.SoftI2C(scl=Pin(SCL), sda=Pin(SDA))
    sleep(.5)
    imu = imu_module.BNO055_BASE(i2c)
    
def imu_calibrated():
    global calibrated
    try:
        if not calibrated:
            sys, gyro, accel, mag = imu.cal_status()
            print(f"Calibrating: gyro[{gyro}] accel[{accel}] mag[{mag}]")
            #calibrated = imu.calibrated()
            calibrated = gyro + mag == 6 # calibrating accel is onerous and (maybe?) unnecessary
            return False
        return True
    except NameError:
        raise Exception("IMU not started")
    
def get_orientation():
    try:
        if imu is False or not calibrated:
            return (0, 0, 0)    
        return imu.euler() # heading, pitch, roll
    except NameError:
        raise Exception("IMU not started")

def get_accel():
    try:
        if imu is False or not calibrated:
            return 0
        return sum([abs(value) for value in imu.lin_acc()])
    except NameError:
        raise Exception("IMU not started")


# SERVOS

def start_servos():
    from servo import Servos
    global servos
    i2c = machine.SoftI2C(scl=Pin(SCL), sda=Pin(SDA))
    servos = Servos(i2c)

class Servo():

    def __init__(self, id):
        self.id = id

    def duty(self):
        return servos.position(self.id)

    def position(self, degrees):
        try:
            current_duty = servos.position(self.id)
            current_degrees = map(current_duty, 491, 1965, 0, 180)
            delta_degrees = abs(degrees - current_degrees)
            servos.position(self.id, degrees)
            sleep(.0035 * delta_degrees)
        except NameError:
            raise Exception("Servos not started")

    def speed(self, speed):
        try:
            servos.position(self.id, (speed * 90) + 90)
        except NameError:
            raise Exception("Servos not started")

        
    def stop(self):
        try:
            servos.release(self.id)
        except NameError:
            raise Exception("Servos not started")


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


def map(value, in_min, in_max, out_min, out_max):
    value = (value - in_min) / float(in_max - in_min)
    return (value * (out_max - out_min)) + out_min


def random(value=None):
    if value is not None:
        return int(rand() * value)
    else:
        return rand()





