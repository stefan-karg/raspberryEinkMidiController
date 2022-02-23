

import digitalio
import busio
import board
from adafruit_epd.epd import Adafruit_EPD
from PIL import Image, ImageDraw, ImageFont

import subprocess

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D22)
rst = digitalio.DigitalInOut(board.D27)
busy = digitalio.DigitalInOut(board.D17)
srcs = None

WHITE = (0xFF, 0xFF, 0xFF)
BLACK = (0x00, 0x00, 0x00)
FONTSIZE = 24


from adafruit_epd.ssd1680 import Adafruit_SSD1680
display = Adafruit_SSD1680(122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=srcs, rst_pin=rst, busy_pin=busy)

display.rotation = 1

display.fill(Adafruit_EPD.WHITE)
image = Image.new("RGB", (display.width, display.height), color=WHITE)
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)


uptime = subprocess.Popen(["uptime", "-p"],
                       stdout=subprocess.PIPE,
                       universal_newlines=True)
uptimeText = uptime.stdout.readline()

draw.text((5, 5), uptimeText, font=font, fill=BLACK)
display.image(image)
display.display()

