#Script for resizing images.

from PIL import Image
from PixelScanner import PixelScanner

image_size = (500, 400, 500 ,400)

image_1 = Image.open("../Photos/1.png")
image_2 = Image.open("../Photos/2.png")
image_3 = Image.open("../Photos/3.png")
image_4 = Image.open("../Photos/4.png")

image_list = [image_1, image_2, image_3, image_4]


pixel_scanner = PixelScanner(image_4)

4_corners = pixel_scanner.get_corners()



top_left_corner = [pixel_scanner.x += 10, pixel_scanner.y += 10]



