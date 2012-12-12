
# STplayer (aka STconverter 2) is under the MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STplayer



import Tkinter

from ..STlibrary import WIDGET



class Button:
    """ Add a button widget on the left side of the frame """
    
    def __init__(self, frame, text, button_handler, width):
        self.button_text = Tkinter.StringVar()
        self.button_text.set(text)
        self = Tkinter.Button(frame, textvariable = self.button_text, 
                              command = button_handler)
        self.config(width = int(width * WIDGET["BUTTON_SIZE_RATIO"]))
        self.pack()
    
    
    def set_text(self, text):
        """ Update the Button label text """
        self.button_text.set(text)
    
    def get_text(self):
        """ Return the Button label text """
        return self.button_text.get()

