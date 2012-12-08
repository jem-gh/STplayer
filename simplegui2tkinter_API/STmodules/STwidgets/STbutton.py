
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



import Tkinter



# SimpleGUI and  Tkinter use different units for Button
# adjust Button size ratio
BUTTON_SIZE_RATIO = 0.09



class Button:
    """ Add a button widget on the left side of the frame """
    
    def __init__(self, frame, text, button_handler, width):
        
        
        self = Tkinter.Button(frame, text = text, command = button_handler)
        self.config(width = int(width * BUTTON_SIZE_RATIO))
        self.pack()
        
        pass




