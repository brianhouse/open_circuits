import esp32, espnow, machine
import network, ubinascii, json, random, socket
from esp32 import hall_sensor  # they took out the hall sensor on recent firmware
from machine import ADC, Pin, TouchPad, PWM
from neopixel import NeoPixel
from time import sleep, ticks_ms
from random import random, randint, choice
from urequests import get, post

# PINS
# https://learn.adafruit.com/adafruit-esp32-feather-v2/pinouts

# A0 = ADC(Pin(26), atten=ADC.ATTN_11DB)  # ADC2
# A1 = ADC(Pin(25), atten=ADC.ATTN_11DB)  # ADC2
A2 = ADC(Pin(34), atten=ADC.ATTN_11DB)
A3 = ADC(Pin(39), atten=ADC.ATTN_11DB)
A4 = ADC(Pin(36), atten=ADC.ATTN_11DB)
# A5 = ADC(Pin(4), atten=ADC.ATTN_11DB)   # ADC2
# A37 = ADC(Pin(37), atten=ADC.ATTN_11DB)


# I/O Pins: 13 (also LED), 12, 27, 33, 15, 32, 14, 21
def IN(pin_n):
    return Pin(pin_n, Pin.IN)


def OUT(pin_n):
    return Pin(pin_n, Pin.OUT)


def CAP(pin_n):
    return TouchPad(Pin(pin_n))


def TONE(pin_n):
    return PWM(OUT(pin_n))


def NEOPIXELS(pin_n=32, num=20, bpp=3):
    return NeoPixel(OUT(pin_n), num, bpp)


SCL = 22  # orig esp32 is 22, v2 is 20, but micropython cant use 20
SDA = 23  # orig esp32 is 23
LED = OUT(13)
# PIX = Pin(0, Pin.OUT)     # V2
# BTN = Pin(38, Pin.IN)  # hardware button, V2
# BAT = ADC(Pin(35), atten=ADC.ATTN_11DB)


def start_wifi():
    global mesh
    global sta
    global udp
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    print("MAC address is", bin_to_hex(sta.config('mac')))
    mesh = espnow.ESPNow()
    mesh.active(True)
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def connect(ssid, pw):
    try:
        if not sta.isconnected():
            print("Connecting to network...")
            try:
                sta.connect(ssid, pw)
            except Exception as e:
                print(e)
            while not sta.isconnected():
                print("...not connected")
                sleep(1)
        print("Network config:", sta.ifconfig())
    except NameError as e:
        print(e)
        print("Wifi not started")


def send_udp(ip, message, port=5005):
    try:
        if not sta.isconnected():
            print("Network not connected")
            return
        udp.sendto(str(message).encode('utf-8'), (ip, port))
    except NameError:
        raise Exception("Wifi not started")
    except Exception as e:
        print("Error:", e)


def add_peer(hex_mac):
    try:
        bin_mac = hex_to_bin(hex_mac)
        mesh.add_peer(bin_mac)
    except NameError:
        raise Exception("Wifi not started")


def send(message):
    try:
        try:
            mesh.send(None, message)
        except Exception:
            print("Can't send")
    except NameError:
        raise Exception("Wifi not started")


def receive():
    try:
        sender, msg = mesh.recv(0)
        if sender is None:
            return None, None
        return bin_to_hex(sender), msg.decode()
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
        return imu.euler()  # heading, pitch, roll
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
            current_degrees = map(current_duty, 470.0, 1965.0, 0.0, 180.0)
            delta_degrees = abs(degrees - current_degrees)
            servos.position(self.id, degrees=degrees)
            sleep(.0035 * delta_degrees)
        except NameError:
            raise Exception("Servos not started")

    def speed(self, speed):
        try:
            speed = map(speed, -1.0, 1.0, -.25, .25)
            servos.position(self.id, map(speed, -1.0, 1.0, 0.0, 180.0))
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

