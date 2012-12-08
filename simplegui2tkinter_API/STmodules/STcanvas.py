
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



import Tkinter

from STdrawing import STtext
from STdrawing import SToval



class Canvas:
    """ Create a canvas widget on the right side of the frame, and handle all 
        user's code methods associated to the canvas ("canvas.xxx"). 
        Called by a redirect from the "create_frame" class which was called from 
        the user's code with the "frame.set_draw_handler" method. """
    
    def __init__(self, frame, canvas_width, canvas_height, background_color):
        """ Create a canvas on the right side of the frame """
        
        self.canvas = Tkinter.Canvas(frame, width = int(canvas_width), 
                                     height = int(canvas_height))
        self.canvas.pack(side = 'right')
        #self.canvas.configure(background = check_color(background_color))
        self.canvas.configure(background = background_color)
    
    
    def new_background_color(self, color):
        """ Set a new background color for the canvas """
        #self.canvas.configure(background = check_color(color))
        self.canvas.configure(background = color)
    
    
    def set_canvas_size(self, width, height):
        """ Set a new width and height for the Canvas """
        self.canvas.config(width = int(width), height = int(height))
    
    
    def set_draw_handler(self, draw_handler):
        """ Set the default drawing handler """
        self.draw_handler = draw_handler
    
    
    def set_refresh_time(self, refresh_time):
        """ Set how often is the Canvas refreshed (in milliseconds) """
        self.refresh_time = refresh_time
    
    
    def refresh_canvas(self):
        """ Refresh the Canvas widget every x milliseconds """
        self.canvas.delete('all')
        self.draw_handler(self)
        self.canvas.after(self.refresh_time, self.refresh_canvas)
    
    
    def draw_text(self, text, position, font_size, font_color):
        """ Call the text class to add a text item on the canvas """
        #font_color = check_color(font_color)
        STtext.Text(self.canvas, text, position, font_size, font_color)
    
    
    def draw_circle(self, center, radius, line_width, line_color, fill_color=""):
        """ Call the oval class to add a circle/oval item on the canvas """
        #line_color, fill_color = check_color(line_color), check_color(fill_color)
        SToval.Oval(self.canvas, center, radius, line_width, line_color, fill_color)


