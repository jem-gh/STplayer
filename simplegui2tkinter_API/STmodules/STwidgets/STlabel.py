
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



import Tkinter



class Label:
    """ Add a label widget on the left side of the frame """
    
    def __init__(self, frame, text, width):
        self.label_text = Tkinter.StringVar()
        self.label_text.set(text)
        self.label = Tkinter.Label(frame, textvariable = self.label_text, 
                                   wraplength = int(width))
        self.label.pack()
    
    
    def set_text(self, text):
        """ Update the label text """
        self.label_text.set(text)

