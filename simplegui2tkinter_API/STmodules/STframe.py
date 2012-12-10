
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



import Tkinter

import STcanvas, STkey
from STwidgets import STlabel, STbutton, STinput



class Frame:
    """ Create the root window with its associated frame and canvas, and handle 
        all user's code methods associated to the frame ("frame.xxx"). 
        Called from the user's code with the "simplegui.create_frame" method. """
    
    def __init__(self, title, canvas_width, canvas_height, control_width = 200):
        """ Initialize the root window, the frame, and the canvas """
        
        self.canvas_width = canvas_width            # by canvas
        self.canvas_height = canvas_height          # by canvas
        self.control_width = control_width          # by label, button, input
        
        # create the root window
        self.window_root = Tkinter.Tk()
        self.window_root.title( title )
        # initialize the frame
        self.frame = Tkinter.Frame(self.window_root)
        # initialize the canvas (of size 0x0) by calling the Canvas class
        self.canvas = STcanvas.Canvas(self.frame, width = 0, height = 0)
    
    
    def start(self):
        """ Display the frame and start the loop event of the root window. """
        self.frame.pack()
        self.window_root.mainloop()
    
    
    def set_draw_handler(self, draw_handler):
        """ Call the Canvas methods to display the canvas, set the drawing 
            handler, and to refresh the drawing. """
        
        # display Canvas by restoring its width and height
        self.canvas.set_canvas_size(self.canvas_width, self.canvas_height)
        # call the Canvas method to set the canvas drawing handler
        self.canvas.set_draw_handler(draw_handler)
        # start the refresh process of the canvas
        self.canvas.refresh_canvas()
    
    
    def set_canvas_background(self, color):
        """ Call the Canvas method to set a new background """
        self.canvas.new_background_color(color)
    
    
    def add_label(self, text):
        """ Call the label class to add a label on the frame """
        return STlabel.Label(self.frame, text, self.control_width)
    
    
    def check_width(self, width):
        """ adjust the width if its larger than the expected control width """
        return self.control_width if self.control_width < width else width
    
    
    def add_button(self, text, button_handler, width = 0):
        """ Call the Button class to add a button on the frame """
        
        width = self.check_width(width)
        return STbutton.Button(self.frame, text, button_handler, width)
    
    
    def add_input(self, text, input_handler, width):
        """ Call the input and label classes to add an input on the frame and 
            its corresponding label """
        
        label = STlabel.Label(self.frame, text, self.control_width)
        width = self.check_width(width)
        STinput.Input(self.frame, input_handler, width)
        return label
    
    
    def set_keydown_handler(self, key_handler):
        """ Call the key class when a key is pressed """
        STkey.Key(self.window_root, '<Key>', key_handler)
    
    
    def set_keyup_handler(self, key_handler):
        """ Call the key class when a key is released """
        STkey.Key(self.window_root, '<KeyRelease>', key_handler)
    
    
    def set_mouseclick_handler(self, mouse_handler):
        """ Forward the left-click mouse event to the Canvas method """
        STcanvas.Canvas.set_mouseclick_handler(self.canvas, mouse_handler)
    
    
    def set_mousedrag_handler(self, mouse_handler):
        """ Forward the drag mouse event to the Canvas method """
        STcanvas.Canvas.set_mousedrag_handler(self.canvas, mouse_handler)


