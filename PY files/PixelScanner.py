#Pixel Scanner

from PIL import Image
from Point import Point

image_width = 0
image_height = 0

class PixelScanner:
    def __init__(self):
        self.image = None

    def contains_colour_range(self, lower, upper, pixel):
        if pixel[0] in range(lower, upper) and pixel[1] in range(lower, upper) and pixel[2] in range(lower, upper):        
            return True
        elif pixel[0] in range(lower, upper) and pixel[1] in range(lower, upper) and pixel[2] in range(lower, upper):        
            return True
        elif pixel[0] in range(lower, upper) and pixel[1] in range(lower, upper) and pixel[2] in range(lower, upper):        
            return True
        elif pixel[0] in range(lower, upper) and pixel[1] in range(lower, upper) and pixel[2] in range(lower, upper):        
            return True
        else:
            return False

    def get_edges(self, image):
        global image_width, image_height

        self.image = image
        image_width = list(self.image.size)[0]
        image_height = list(self.image.size)[1]

        edges = []

        left_point = Point(0, (image_height / 2))
        top_point = Point((image_width / 2), 0)
        right_point = Point((image_width - 1), (image_height / 2))
        bottom_point = Point((image_width / 2), (image_height - 1))

        left_pixel = self.image.getpixel((left_point.x, left_point.y))
        top_pixel = self.image.getpixel((top_point.x, top_point.y))
        right_pixel = self.image.getpixel((right_point.x, right_point.y))
        bottom_pixel = self.image.getpixel((bottom_point.x, bottom_point.y))

        final_left_point = None
        final_top_point = None
        final_right_point = None
        final_bottom_point = None

        while final_left_point == None:
            if self.contains_colour_range(0, 200, left_pixel):
                final_left_point = Point((left_point.x - 2), left_point.y)
                edges.append(final_left_point)
            else:
                left_point.shift(1, 0)
                left_pixel = self.image.getpixel((left_point.x, left_point.y))

        while final_top_point == None:
            if self.contains_colour_range(0, 200, top_pixel):
                final_top_point = Point(top_point.x, (top_point.y - 2))
                edges.append(final_top_point)
            else:
                top_point.shift(0, 1)
                top_pixel = self.image.getpixel((top_point.x, top_point.y))

        while final_right_point == None:
            if self.contains_colour_range(0, 200, right_pixel):
                final_right_point = Point((right_point.x + 2), right_point.y)
                edges.append(final_right_point)
            else:
                right_point.shift(-1, 0)
                right_pixel = self.image.getpixel((right_point.x, right_point.y))

        while final_bottom_point == None:
            if self.contains_colour_range(0, 200, bottom_pixel):
                final_bottom_point = Point(bottom_point.x, (bottom_point.y + 2))
                edges.append(final_bottom_point)
            else:
                bottom_point.shift(0, -1)
                bottom_pixel = self.image.getpixel((bottom_point.x, bottom_point.y))

        return edges