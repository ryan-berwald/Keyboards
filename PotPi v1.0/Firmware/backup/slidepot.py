# Write your code here :-)
from adafruit_hid.keyboard import Keyboard
from kmk.keys import KC
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl

import time
import board
from analogio import AnalogIn
#GP27 GP276

pot1 = AnalogIn(board.GP27)
pot2 = AnalogIn(board.GP26)

refVolt = pot2.reference_voltage

while True:

    print((pot1.value, pot2.value, pot1.reference_voltage, pot2.reference_voltage))      # Display value

    time.sleep(1)                   # Wait a bit before checking all again



