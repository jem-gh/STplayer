
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



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
        """ Update the label text """
        self.button_text.set(text)

