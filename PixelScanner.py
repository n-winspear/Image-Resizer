#Pixel Scanner
from PIL import Image
import Point

class PixelScanner:
	def __init__(self, image):
		self.image = image
		self.x
		self.y
		self.TLPixel = image.getpixel(x, y) 
		self.TRPixel = image.getpixel(x + 1, y)
		self.BLPixel = image.getpixel(x, y + 1)
		self.BRPixel = image.getpixel(x + 1, y + 1)

	def __repr__(self):
		return f"TL: {TLPixel} TR: {TRPixel} BL: {BLPixel} BR: {BRPixel}"

	def checkcolourrange(self, lower, upper):
		if self.TLPixel[0] in range(lower, upper) && self.TLPixel[1] in range(lower, upper) && self.TLPixel[2] in range(lower, upper):		
			return True
		else if self.TRPixel[0] in range(lower, upper) && self.TRPixel[1] in range(lower, upper) && self.TRPixel[2] in range(lower, upper):		
			return True
		else if self.BLPixel[0] in range(lower, upper) && self.BLPixel[1] in range(lower, upper) && self.BLPixel[2] in range(lower, upper):		
			return True
		else if self.BRPixel[0] in range(lower, upper) && self.BRPixel[1] in range(lower, upper) && self.BRPixel[2] in range(lower, upper):		
			return True
		else:
			return False

	def shift(self):
		




