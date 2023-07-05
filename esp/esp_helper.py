import esp32, espnow, json
import network, ubinascii
from esp32 import hall_sensor
from machine import ADC, Pin, TouchPad, PWM
from time import sleep, time


# set up pins
# https://learn.adafruit.com/adafruit-huzzah32-esp32-feather/pinouts
A2 = ADC(Pin(34), atten=ADC.ATTN_11DB)
A3 = ADC(Pin(39), atten=ADC.ATTN_11DB)
A4 = ADC(Pin(36), atten=ADC.ATTN_11DB)
D32 = Pin(32)
D33 = Pin(33)
S21 = Pin(21, Pin.OUT)
S27 = Pin(27, Pin.OUT)
LED = Pin(13, Pin.OUT)
T12 = TouchPad(Pin(12))
T14 = TouchPad(Pin(14))
T15 = TouchPad(Pin(15))


# configure p2p networking
sta = network.WLAN(network.STA_IF)
sta.active(True)
hex_mac = ubinascii.hexlify(sta.config('mac'), ':').decode().upper()
print("MAC address is", hex_mac)
e = espnow.ESPNow()
e.active(True)
bcast = b'\xff' * 6
e.add_peer(bcast)

def send(message):
    print("Sending", message)
    e.send(bcast, message)

def receive():
    host, msg = e.recv(0)
    if msg:
        mac = ubinascii.hexlify(host, ':').decode().upper()
        return mac, msg.decode()
    else:
        return None, None


# utility classes
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






