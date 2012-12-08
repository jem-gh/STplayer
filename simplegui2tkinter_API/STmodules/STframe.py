
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



import Tkinter



import STcanvas
import STtimer
from STwidgets import STbutton



# Canvas background default color
CANVAS_BACKGROUND = "Black"

# Adjust the Canvas refresh time
CANVAS_REFRESH_TIME = 17 # in ms (66ms~15fps; 33ms~30fps; 17ms~60fps)



class Frame:
    """ Create the root window with its associated frame and canvas, and handle 
        all user's code methods associated to the frame ("frame.xxx"). 
        Called from the user's code with the "simplegui.create_frame" method. """
    
    def __init__(self, title, canvas_width, canvas_height, control_width = 200):
        """ Initialize the root window, the frame, and the canvas """
        
        self.canvas_width = canvas_width            # by canvas
        self.canvas_height = canvas_height          # by canvas
        self.canvas_background = CANVAS_BACKGROUND  # by canvas
        self.control_width = control_width          # by label, button, input
        
        # create the window_root
        self.window_root = Tkinter.Tk()
        self.window_root.title( title )
        # initialize the frame
        self.frame = Tkinter.Frame(self.window_root)
        # initialize the canvas by calling the Canvas class
        self.canvas = STcanvas.Canvas(self.frame, 0, 0, self.canvas_background)
    
    
    def start(self):
        """ Display the frame and start the loop event of the root window. """
        self.frame.pack()
        self.window_root.mainloop()
    
    
    def set_draw_handler(self, draw_handler):
        """ Call the canvas methods to display the canvas, set the drawing 
            handler, and to refresh the drawing. """
        
        # Display Canvas by restoring its width and height
        self.canvas.set_canvas_size(self.canvas_width, self.canvas_height)
        
        # call the canvas method to set the Canvas drawing handler
        self.canvas.set_draw_handler(draw_handler)
        
        # start the refresh process of the Canvas
        self.canvas.set_refresh_time(CANVAS_REFRESH_TIME)
        self.canvas.refresh_canvas()
    
    
    def add_button(self, text, button_handler, width = 0):
        """ Call the Button class to add a button on the frame """
        
        # adjust the width if its larger than the expected control width 
        width = self.control_width if self.control_width < width else width
        
        STbutton.Button(self.frame, text, button_handler, width)


