
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



class Oval:
    """ Add an oval item on the canvas """
    
    def __init__(self, canvas, center, radius, line_width, line_color, fill_color):
        
        # go from a center-radius reference to an ellipse coordinates
        x, y = center
        coordinates = ((x - radius), (y - radius), (x + radius), (y + radius))
        
        canvas.create_oval(coordinates, width = line_width, 
                           outline = line_color, fill = fill_color)



