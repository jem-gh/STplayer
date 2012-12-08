
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



class Polygon:
    """ Add a polygon item on the canvas """
    
    def __init__(self, canvas, points, line_width, line_color, fill_color):
        canvas.create_polygon(points, width = int(line_width), 
                              outline = line_color, fill = fill_color)

