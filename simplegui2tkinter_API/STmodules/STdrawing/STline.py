
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



def line(canvas, points, line_width, line_color):
    """ Add a line item on the canvas """
    
    # duplicate first point in case only one point was given
    points = points[0], points
    canvas.create_line(points, width = int(line_width), fill = line_color)

