# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, and some white text.
"""

import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import busio

class oled:
    def __init__(self, SDA, SCL, oText):
        releaseDisp()
        self.oText = oText
        self.i2c = busio.I2C(SDA, SCL)
        self.display_bus = displayio.I2CDisplay(self.i2c, device_address=0x3C)
        self.display = adafruit_displayio_ssd1306.SSD1306(self.display_bus, width=128, height=32)


    def updateOLED(self, active_layer):
        # Make the display context
        splash = displayio.Group(max_size=10)
        self.display.show(splash)

        color_bitmap = displayio.Bitmap(128, 32, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        splash.append(bg_sprite)

        # Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(118, 24, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
        splash.append(inner_sprite)

        # Draw a label        text = self.oText
        text_area = label.Label(terminalio.FONT, text="Active Layer: " + str(active_layer), color=0xFFFF00, x=28, y=15)
        splash.append(text_area)

def releaseDisp():
        displayio.release_displays()

