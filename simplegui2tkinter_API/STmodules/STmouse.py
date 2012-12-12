
# STplayer (aka STconverter 2) is under the MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STplayer



class Mouse:
    """ Retrieve the mouse coordinate during a mouse event (click or drag) """
    
    def __init__(self, target, mode, mouse_handler):
        self.mouse_handler = mouse_handler
        target.bind(mode, self.call_handler)
    
    def call_handler(self, coordinate):
        """ Return the coordinate of the mouse """
        self.mouse_handler( (coordinate.x, coordinate.y) )


