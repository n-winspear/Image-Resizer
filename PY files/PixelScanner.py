#Pixel Scanner

from PIL import Image
from Point import Point

image_width = 0
image_height = 0

class PixelScanner:
    def __init__(self):
        self.image = None

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
        #print("5", str(self.TLPixel), str(self.TRPixel), str(self.BLPixel), str(self.BRPixel))
        return corners

    def contains_colour_range(self, lower, upper, TLPixel, TRPixel, BLPixel, BRPixel):
        if TLPixel[0] in range(lower, upper) and TLPixel[1] in range(lower, upper) and TLPixel[2] in range(lower, upper):        
            return True
        elif TRPixel[0] in range(lower, upper) and TRPixel[1] in range(lower, upper) and TRPixel[2] in range(lower, upper):        
            return True
        elif BLPixel[0] in range(lower, upper) and BLPixel[1] in range(lower, upper) and BLPixel[2] in range(lower, upper):        
            return True
        elif BRPixel[0] in range(lower, upper) and BRPixel[1] in range(lower, upper) and BRPixel[2] in range(lower, upper):        
            return True
        else:
            return False

    def get_top_left(self):

        x = 0
        y = 0

        TLPixel = self.image.getpixel( (x, y) ) 
        TRPixel = self.image.getpixel( (x + 1, y) )
        BLPixel = self.image.getpixel( (x, y + 1) )
        BRPixel = self.image.getpixel( (x + 1, y + 1) )

        for pixel_set in range(100):
            if self.contains_colour_range(0, 200, TLPixel, TRPixel, BLPixel, BRPixel):
                x += 3
                y += 3
                return Point(x, y)
            else:
                x += 1
                y += 1
                TLPixel = self.image.getpixel( (x, y) ) 
                TRPixel = self.image.getpixel( (x + 1, y) )
                BLPixel = self.image.getpixel( (x, y + 1) )
                BRPixel = self.image.getpixel( (x + 1, y + 1) )

    def get_top_right(self):
        global image_width, image_height

        x = image_width - 1
        y = 0

        TLPixel = self.image.getpixel( (x - 1, y) ) 
        TRPixel = self.image.getpixel( (x, y) )
        BLPixel = self.image.getpixel( (x - 1, y + 1) )
        BRPixel = self.image.getpixel( (x, y + 1) )

        for pixel_set in range(100):
            if self.contains_colour_range(0, 200, TLPixel, TRPixel, BLPixel, BRPixel):
                x -= 3
                y += 3
                return Point(x, y)
            else:
                x -= 1
                y += 1
                TLPixel = self.image.getpixel( (x - 1, y) ) 
                TRPixel = self.image.getpixel( (x, y) )
                BLPixel = self.image.getpixel( (x - 1, y + 1) )
                BRPixel = self.image.getpixel( (x, y + 1) )

    def get_bottom_left(self):
        global image_width, image_height

        x = 0
        y = image_height - 1

        TLPixel = self.image.getpixel( (x, y - 1) ) 
        TRPixel = self.image.getpixel( (x + 1, y - 1) )
        BLPixel = self.image.getpixel( (x, y) )
        BRPixel = self.image.getpixel( (x + 1, y) )

        for pixel_set in range(100):
            if self.contains_colour_range(0, 200, TLPixel, TRPixel, BLPixel, BRPixel):
                x += 3
                y -= 3
                return Point(x, y)
            else:
                x += 1
                y -= 1
                TLPixel = self.image.getpixel( (x, y - 1) ) 
                TRPixel = self.image.getpixel( (x + 1, y - 1) )
                BLPixel = self.image.getpixel( (x, y) )
                BRPixel = self.image.getpixel( (x + 1, y) )

    def get_bottom_right(self):
        global image_width, image_height

        x = image_width - 1
        y = image_height - 1

        TLPixel = self.image.getpixel( (x - 1, y - 1) ) 
        TRPixel = self.image.getpixel( (x, y - 1) )
        BLPixel = self.image.getpixel( (x - 1, y) )
        BRPixel = self.image.getpixel( (x, y) )

        for pixel_set in range(100):
            if self.contains_colour_range(0, 200, TLPixel, TRPixel, BLPixel, BRPixel):
                x -= 3
                y -= 3
                return Point(x, y)
            else:
                x -= 1
                y -= 1
                TLPixel = self.image.getpixel( (x - 1, y - 1) ) 
                TRPixel = self.image.getpixel( (x, y - 1) )
                BLPixel = self.image.getpixel( (x - 1, y) )
                BRPixel = self.image.getpixel( (x, y) )





