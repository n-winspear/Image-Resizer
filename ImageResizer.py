#Script for resizing images.

from PIL import Image
from  import PixelScanner
 
image_size = (500, 400, 500 ,400)

image_1 = Image.open("Photos/1.png")
image_2 = Image.open("Photos/2.png")
image_3 = Image.open("Photos/3.png")
image_4 = Image.open("Photos/4.png")

image_list = [image_1, image_2, image_3, image_4]

pixel_scanner = PixelScanner(image_4, TLPixel, TRPixel, BLPixel, BRPixel)

for pixel_set in range(100):
	if pixel_scanner.containscolourrange(0, 100):
		print("DO SOMETHING HERE")
	else:
		pixel_scanner.shift()