
# STplayer (aka STconverter 2) is under the MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STplayer



import Tkinter

from ..STlibrary import WIDGET



class Input:
    """ Add an input widget on the left side of the frame """
    
    def __init__(self, frame, input_handler, width):
        
        self.input_handler = input_handler
        
        self.input = Tkinter.Entry(frame)
        self.input.bind('<Return>', self.call_handler)
        self.input.config(width = int(width * WIDGET["INPUT_SIZE_RATIO"]))
        self.input.pack()
    
    def call_handler(self, input_value):
        """ Return the value entered in the input to the input handler """
        self.input_handler(self.input.get())

