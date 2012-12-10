
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



try:
    from PIL import Image, ImageTk
except ImportError:
    print "Python Imaging Library (PIL) not found"



def create_ID(params):
    """ return a string which is unique to the parameters given """
    return ','.join(str(param) for param in params)



class Image_process:
    """ Store, process, and convert images to a Tkinter-compatible format by 
        using the Python Imaging Library (PIL). 
        Actual image processing operations are: crop, resize, rotate. 
        Both images and their processed results are stored for a faster re-use. 
        
        src_coor, src_size = center coordinates (x, y) and size (width, height) 
                             in pixels of a selection of the source image 
        dest_size = size (width, height) in pixels on the canvas of the 
                    selected part of the image 
        angle = angle in radians of clockwise rotation around its center """
    
    def __init__(self, image):
        self.image = Image.open( image )
        
        # convert "P" mode images to "RGBA" mode
        if self.image.mode == "P":
            self.image = self.image.convert("RGBA")
        
        self.tiles = {}
    
    
    def process(self, src_coor, src_size, dest_size, angle_d, ID):
        """ Crop, resize, rotate an image, and convert it in Tkinter format """
        
        x1, y1 = (src_coor[0]-src_size[0]/2), (src_coor[1]-src_size[1]/2)
        x2, y2 = (src_coor[0]+src_size[0]/2), (src_coor[1]+src_size[1]/2)
        # crop
        processed = self.image.crop((int(x1), int(y1), int(x2), int(y2)))
        # resize
        if dest_size != src_size:
            size = [int(dest_size[0]), int(dest_size[1])]
            processed = processed.resize(size, resample=Image.BILINEAR)
        # rotate
        if angle_d:
            processed = processed.rotate(-angle_d, resample=Image.BICUBIC, expand=1)
        # store
        self.tiles[ID] = ImageTk.PhotoImage(processed)
    
    
    def update(self, src_coor, src_size, dest_size, angle):
        """ return a processed image with a defined size and angle """
        
        # convert angle from radians to degrees
        angle_d = int((angle * 180 / 3.1416) % 360)
        # create the rendering image ID
        ID = create_ID([src_coor, src_size, dest_size, angle_d])
        # process the image if it doesn't already exist
        if ID not in self.tiles:
            self.process(src_coor, src_size, dest_size, angle_d, ID)
        # return the processed image
        return self.tiles[ID]
    
    
    def get_width(self):
        """ return the width of the source image in pixels """
        return self.image.size[0]
    
    
    def get_height(self):
        """ return the height of the source image in pixels """
        return self.image.size[1]


