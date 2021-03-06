

import digitalio
import busio
import board
from adafruit_epd.epd import Adafruit_EPD
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import subprocess

class Eink:

	spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
	ecs = digitalio.DigitalInOut(board.CE0)
	dc = digitalio.DigitalInOut(board.D22)
	rst = digitalio.DigitalInOut(board.D27)
	busy = digitalio.DigitalInOut(board.D17)
	srcs = None

	display = None
	
	logCount = 0


	def init(self):
		from adafruit_epd.ssd1680 import Adafruit_SSD1680
		self.display = Adafruit_SSD1680(122, 250, self.spi, cs_pin=self.ecs, dc_pin=self.dc, sramcs_pin=self.srcs, rst_pin=self.rst, busy_pin=self.busy)

		self.display.rotation = 1
		
		self.display.fill(Adafruit_EPD.WHITE)
		
	def clearWhite(self):
		self.display.fill(Adafruit_EPD.WHITE)
		
	def clearBlack(self):
		self.display.fill(Adafruit_EPD.BLACK)
		
		
	def lcdText(self, text, x=0, y=0, color=Adafruit_EPD.BLACK, textsize=2):
		self.display.text(text, x, y, Adafruit_EPD.BLACK, size=textsize)
		
	def logText(self, text):
		if self.logCount >= 4:
			self.logCount = 0
			self.clearWhite()
			
		self.display.text(text, 1, self.logCount * 18, Adafruit_EPD.BLACK, size=2)
		self.logCount = self.logCount + 1
		
	def text(self):
		print("None")
		
	def update(self):
		self.display.display()
		
	def test_func(self):

		self.display.fill(Adafruit_EPD.WHITE)
		

		uptime = subprocess.Popen(["uptime", "-p"],
				       stdout=subprocess.PIPE,
				       universal_newlines=True)
		uptimeText = uptime.stdout.readline()

		draw.text((5, 5), uptimeText, font=font, fill=self.BLACK)
		self.display.text("Hallo my Love! <3", 25, 10, Adafruit_EPD.BLACK, size=2)
		#display.image(image)
		self.display.display()

