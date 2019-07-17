#Pixel Scanner
from PIL import Image

global image_width
global image_height

class PixelScanner:
	def __init__(self):
		self.x = 0 
		self.y = 0

	def __repr__(self):
		return f("TL: {TLPixel} TR: {TRPixel} BL: {BLPixel} BR: {BRPixel})")

	def get_corners(self, image):
		image_width, image_height = image.size()
		corners = []
		corners[0] = get_top_left()
		corners[1] = get_top_right()
		corners[2] = get_bottom_left()
		corners[3] = get_bottom_right()
		return corners

	def contains_colour_range(self, lower, upper):
		if self.TLPixel[0] in range(lower, upper) and self.TLPixel[1] in range(lower, upper) and self.TLPixel[2] in range(lower, upper):		
			return True
		elif self.TRPixel[0] in range(lower, upper) and self.TRPixel[1] in range(lower, upper) and self.TRPixel[2] in range(lower, upper):		
			return True
		elif self.BLPixel[0] in range(lower, upper) and self.BLPixel[1] in range(lower, upper) and self.BLPixel[2] in range(lower, upper):		
			return True
		elif self.BRPixel[0] in range(lower, upper) and self.BRPixel[1] in range(lower, upper) and self.BRPixel[2] in range(lower, upper):		
			return True
		else:
			return False

	def get_top_left():
		self.TLPixel = self.image.getpixel( (self.x, self.y) ) 
		self.TRPixel = self.image.getpixel( (self.x + 1, self.y) )
		self.BLPixel = self.image.getpixel( (self.x, self.y + 1) )
		self.BRPixel = self.image.getpixel( (self.x + 1, self.y + 1) )

		for pixel_set in range(100):
			if contains_colour_range(0, 100):
				return [self.x += 10, self.y += 10]
			else:
				shift("DR")

	def get_top_right():
		self.x = image_width
		self.y = 0
		self.TLPixel = self.image.getpixel( (self.x - 1, self.y) ) 
		self.TRPixel = self.image.getpixel( (self.x, self.y) )
		self.BLPixel = self.image.getpixel( (self.x - 1, self.y + 1) )
		self.BRPixel = self.image.getpixel( (self.x, self.y + 1) )

		for pixel_set in range(100):
			if contains_colour_range(0, 100):
				return [self.x -= 10, self.y += 10]
			else:
				shift("DL")



	def shift(self, shift_direction):
		if shift_direction == "DR":
			self.x += 1
			self.y += 1
			self.TLPixel = self.image.getpixel( (self.x, self.y) ) 
			self.TRPixel = self.image.getpixel( (self.x + 1, self.y) )
			self.BLPixel = self.image.getpixel( (self.x, self.y + 1) )
			self.BRPixel = self.image.getpixel( (self.x + 1, self.y + 1) )	
			return

		elif shift_direction == "DL":
			self.x -= 1
			self.y += 1
			self.TLPixel = self.image.getpixel( (self.x - 1, self.y) ) 
			self.TRPixel = self.image.getpixel( (self.x, self.y) )
			self.BLPixel = self.image.getpixel( (self.x - 1, self.y + 1) )
			self.BRPixel = self.image.getpixel( (self.x, self.y + 1) )

			

		





