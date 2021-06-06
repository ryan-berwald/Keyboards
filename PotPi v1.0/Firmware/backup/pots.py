# Write your code here :-)
import time
import board
from analogio import AnalogIn

potentiometer = AnalogIn(board.GP26) # potentiometer connected to A1, power & ground
potentiometer2 = AnalogIn(board.GP27)

while True:

    print((potentiometer.value, potentiometer2.value))      # Display value

    time.sleep(0.25)                   # Wait a bit before checking all again
