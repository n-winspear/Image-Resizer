#Script for resizing images.

from PIL import Image
from PixelScanner import PixelScanner
import os

def get_paste_box(edges):
		    left_x = edges[0].x
		    top_y = edges[1].y
		    right_x = edges[2].x
		    bottom_y = edges[3].y
		    paste_box = (left_x, top_y, right_x, bottom_y)
		    return paste_box

def add_background(cropped_image):
    max_image_size = (400, 500)
    cropped_image.thumbnail(max_image_size)
    offset = (0, (500 - (list(cropped_image.size)[1])) // 2)
    background = Image.new("RGBA", (400, 500), (255, 255, 255, 255))
    background.paste(cropped_image, offset)
    return background

for folder in os.listdir("C:/Users/nwins/Documents/GitHub/Image-Resizer/Originals"):
	folder_name = str(folder)
	counter = 1
	pixel_scanner = PixelScanner()
	for image in os.listdir("C:/Users/nwins/Documents/GitHub/Image-Resizer/Originals/{}".format(folder)):
		working_image = Image.open("C:/Users/nwins/Documents/GitHub/Image-Resizer/Originals/{}/{}".format(folder_name, image))
		edges = pixel_scanner.get_edges(working_image)
		paste_box = get_paste_box(edges)
		cropped_image = working_image.crop(paste_box)
		final_image = add_background(cropped_image)
		file_name = "{}_{}.png".format(folder_name, counter)
		final_image.save("C:/Users/nwins/Documents/GitHub/Image-Resizer/Processed/{}/{}".format(folder_name, file_name))
		counter += 1
