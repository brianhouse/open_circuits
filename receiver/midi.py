#!/usr/bin/env python3

import sys, time, threading, queue, rtmidi
from rtmidi.midiconstants import NOTE_ON, NOTE_OFF, CONTROLLER_CHANGE

log_midi = True

class MidiOut(threading.Thread):

    def __init__(self, interface=0, throttle=0):
        threading.Thread.__init__(self)
        self.daemon = True
        self._interface = interface
        self.throttle = throttle
        self.queue = queue.Queue()
        self.midi = rtmidi.MidiOut()
        available_interfaces = self.scan()
        if available_interfaces:
            if self._interface >= len(available_interfaces):
                print("Interface index %s not available" % self._interface)
                return
            print("MIDI OUT: %s" % available_interfaces[self._interface])
            self.midi.open_port(self._interface)
        else:
            print("MIDI OUT opening virtual interface 'Firefly'...")
            self.midi.open_virtual_port('Firefly')
        self.start()

    def scan(self):
        available_interfaces = self.midi.get_ports()
        if len(available_interfaces):
            print("MIDI outputs available: %s" % available_interfaces)
        else:
            print("No MIDI outputs available")
        return available_interfaces

    def send_control(self, channel, control, value):
        self.queue.put((channel, (control, value), None))

    def send_note(self, channel, pitch, velocity):
        self.queue.put((channel, None, (pitch, velocity)))

    @property
    def interface(self):
        return self._interface

    @interface.setter
    def interface(self, interface):
        self.__init__(interface=interface, throttle=self.throttle)

    def run(self):
        while True:
            channel, control, note = self.queue.get()
            if control is not None:
                control, value = control
                if type(value) == bool:
                    value = 127 if value else 0
                if log_midi:
                    print("MIDI ctrl %s %s %s" % (channel, control, value))
                channel -= 1
                self.midi.send_message([CONTROLLER_CHANGE | (channel & 0xF), control, value])
            if note is not None:
                pitch, velocity = note
                if log_midi:
                    print("MIDI note %s %s %s" % (channel, pitch, velocity))
                channel -= 1
                if velocity:
                    self.midi.send_message([NOTE_ON | (channel & 0xF), pitch & 0x7F, velocity & 0x7F])
                else:
                    self.midi.send_message([NOTE_OFF | (channel & 0xF), pitch & 0x7F, 0])
            if self.throttle > 0:
                time.sleep(self.throttle)



midi_out = MidiOut(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
print("MIDI ready")
