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







