#Script for resizing images.

from PIL import Image
from PixelScanner import PixelScanner

image_1 = Image.open("../Photos/1.png")
image_2 = Image.open("../Photos/2.png")
image_3 = Image.open("../Photos/3.png")
image_4 = Image.open("../Photos/4.png")

image_list = [image_1, image_2, image_3, image_4]

pixel_scanner = PixelScanner()

def get_paste_box(edges):
    left_x = edges[0].x
    top_y = edges[1].y
    right_x = edges[2].x
    bottom_y = edges[3].y
    paste_box = (left_x, top_y, right_x, bottom_y)
    return paste_box


for img in range(len(image_list)):
    edges = pixel_scanner.get_edges(image_list[img])
    paste_box = get_paste_box(edges)
    cropped_image = image_list[img].crop(paste_box)
    file_name = "{}.png".format(img)
    cropped_image.save("../Output/{}".format(file_name))

