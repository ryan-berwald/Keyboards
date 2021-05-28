from adafruit_hid.keyboard import Keyboard
from kmk.keys import KC
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl

import analogio
import board
#GP27 GP276

class slider:
    def __init__(self, pin):
        self.pin = pin

    def printV (self) :
        print(self.value)

consumerKeys = [226, 233, 234, 181, 182, 183]

