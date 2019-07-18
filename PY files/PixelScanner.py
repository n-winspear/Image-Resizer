#Pixel Scanner

from PIL import Image
from Point import Point

image_width = 0
image_height = 0
x = 0
y = 0

class PixelScanner:
	def __init__(self):
		self.image = None
		self.TLPixel = None
		self.TRPixel = None
		self.BLPixel = None
		self.BRPixel = None

	def __repr__(self):
		return ("PixelScanner Currently At: ({0}, {1})".format(x, y))

	def get_corners(self, image):
		global image_width, image_height

		self.image = image
		image_width = list(self.image.size)[0]
		image_height = list(self.image.size)[1]

		corners = []
		corners.insert(0, self.get_top_left())
		corners.insert(1, self.get_top_right())
		corners.insert(2, self.get_bottom_left())
		corners.insert(3, self.get_bottom_right())
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

	def get_top_left(self):
		global x, y, image_width, image_height

		self.TLPixel = self.image.getpixel( (x, y) ) 
		self.TRPixel = self.image.getpixel( (x + 1, y) )
		self.BLPixel = self.image.getpixel( (x, y + 1) )
		self.BRPixel = self.image.getpixel( (x + 1, y + 1) )

		for pixel_set in range(100):
			if self.contains_colour_range(0, 200):
				x += 3
				y += 3
				return Point(x, y)
			else:
				self.shift("DR")

	def get_top_right(self):
		global x, y, image_width, image_height

		x = image_width - 1
		y = 0

		self.TLPixel = self.image.getpixel( (x - 1, y) ) 
		self.TRPixel = self.image.getpixel( (x, y) )
		self.BLPixel = self.image.getpixel( (x - 1, y + 1) )
		self.BRPixel = self.image.getpixel( (x, y + 1) )

		for pixel_set in range(100):
			if self.contains_colour_range(0, 200):
				x -= 3
				y += 3
				return Point(x, y)
			else:
				self.shift("DL")

	def get_bottom_left(self):
		global x, y, image_width, image_height

		x = 0
		y = image_height - 1

		self.TLPixel = self.image.getpixel( (x, y - 1) ) 
		self.TRPixel = self.image.getpixel( (x + 1, y - 1) )
		self.BLPixel = self.image.getpixel( (x, y) )
		self.BRPixel = self.image.getpixel( (x + 1, y) )

		for pixel_set in range(100):
			if self.contains_colour_range(0, 200):
				x += 3
				y -= 3
				return Point(x, y)
			else:
				self.shift("UR")

	def get_bottom_right(self):
		global x, y, image_width, image_height

		x = image_width - 1
		y = image_height - 1

		self.TLPixel = self.image.getpixel( (x - 1, y - 1) ) 
		self.TRPixel = self.image.getpixel( (x, y - 1) )
		self.BLPixel = self.image.getpixel( (x - 1, y) )
		self.BRPixel = self.image.getpixel( (x, y) )

		for pixel_set in range(100):
			if self.contains_colour_range(0, 200):
				x -= 3
				y -= 3
				return Point(x, y)
			else:
				self.shift("UL")

	def shift(self, shift_direction):
		global x, y, image_width, image_height

		if shift_direction == "DR":
			x += 1
			y += 1
			self.TLPixel = self.image.getpixel( (x, y) ) 
			self.TRPixel = self.image.getpixel( (x + 1, y) )
			self.BLPixel = self.image.getpixel( (x, y + 1) )
			self.BRPixel = self.image.getpixel( (x + 1, y + 1) )
			return	

		elif shift_direction == "DL":
			x -= 1
			y += 1
			self.TLPixel = self.image.getpixel( (x - 1, y) ) 
			self.TRPixel = self.image.getpixel( (x, y) )
			self.BLPixel = self.image.getpixel( (x - 1, y + 1) )
			self.BRPixel = self.image.getpixel( (x, y + 1) )
			return

		elif shift_direction == "UR":
			x += 1
			y -= 1
			self.TLPixel = self.image.getpixel( (x, y - 1) ) 
			self.TRPixel = self.image.getpixel( (x + 1, y - 1) )
			self.BLPixel = self.image.getpixel( (x, y) )
			self.BRPixel = self.image.getpixel( (x + 1, y) )
			return

		elif shift_direction == "UL":
			x -= 1
			y -= 1
			self.TLPixel = self.image.getpixel( (x - 1, y - 1) ) 
			self.TRPixel = self.image.getpixel( (x, y - 1) )
			self.BLPixel = self.image.getpixel( (x - 1, y) )
			self.BRPixel = self.image.getpixel( (x, y) )
			return
			

		





