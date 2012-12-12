
# STplayer (aka STconverter 2) is under the MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STplayer



def polygon(canvas, points, line_width, line_color, fill_color):
    """ Add a polygon item on the canvas """
    
    canvas.create_polygon(points, width = int(line_width), 
                          outline = line_color, fill = fill_color)

