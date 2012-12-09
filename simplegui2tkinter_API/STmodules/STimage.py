
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



from PIL import Image, ImageTk



def create_ID(params):
    """ return a string which is unique to the parameters given """
    return ','.join(str(param) for param in params)



class Image_process:
    """ Store, process, and convert images to a Tkinter-compatible format. 
        Actual image processing operations are: crop, resize, rotate. 
        Both images and their processed results are stored for a faster re-use. 
        
        src_coor, src_size = center coordinates (x, y) and size (width, height) 
                             in pixels of a selection of the source image 
        dest_size = size (width, height) in pixels on the canvas of the 
                    selected part of the image 
        angle = angle in radians of clockwise rotation around its center """
    
    def __init__(self, image):
        self.img = image
        self.tiles = {}
    
    
    def process(self, src_coor, src_size, dest_size, angle_d, ID):
        x1, y1 = (src_coor[0]-src_size[0]/2), (src_coor[1]-src_size[1]/2)
        x2, y2 = (src_coor[0]+src_size[0]/2), (src_coor[1]+src_size[1]/2)
        # crop
        processed = self.img.crop((int(x1), int(y1), int(x2), int(y2)))
        # resize
        if dest_size != src_size:
            processed = processed.resize(dest_size, resample=Image.BILINEAR)
        # rotate
        if angle_d:
            processed = processed.rotate(-angle_d, resample=Image.BICUBIC, expand=1)
        # store
        self.tiles[ID] = ImageTk.PhotoImage(processed)
    
    
    def update(self, src_coor, src_size, dest_size, angle):
        # convert angle from radians to degrees
        angle_d = int((angle * 180 / 3.1416) % 360)
        # create the rendering image ID
        ID = create_ID([src_coor, src_size, dest_size, angle_d])
        # process the image if it doesn't already exist
        if ID not in self.tiles:
            self.process(src_coor, src_size, dest_size, angle_d, ID)
        # return the processed image
        return self.tiles[ID]


