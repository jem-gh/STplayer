
# STplayer (aka STconverter 2) is under the MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STplayer



def oval(canvas, center, radius, line_width, line_color, fill_color):
    """ Add an oval item on the canvas """
    
    # go from a center-radius reference to an ellipse coordinates
    coordinates = (int(center[0] - radius), int(center[1] - radius), 
                   int(center[0] + radius), int(center[1] + radius))
    
    canvas.create_oval(coordinates, width = int(line_width), 
                       outline = line_color, fill = fill_color)



