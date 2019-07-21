#Script for resizing images.

from PIL import Image
from PixelScanner import PixelScanner

image_1 = Image.open("../Photos/1.png")
image_2 = Image.open("../Photos/2.png")
image_3 = Image.open("../Photos/3.png")
image_4 = Image.open("../Photos/4.png")
image_5 = Image.open("../Photos/5.png")

image_list = [image_1, image_2, image_3, image_4, image_5]

def get_crop_box(corners):
	crop_width = corners[0].x - corners[1].x
	crop_height = corners[0].y - corners[3].y
	crop_box = (corners[0].x, corners[0].y, crop_width, crop_height)
	#print(crop_box)
	return crop_box

pixel_scanner = PixelScanner()

for img in range(len(image_list)):
    corners = pixel_scanner.get_corners(image_list[img])
    crop_box = get_crop_box(corners)
    print(corners)
    cropped_image = image_list[img].crop(crop_box)
    file_name = "{}.png".format(img)
    print(file_name + "Saved")
    #cropped_image.save(file_name)

