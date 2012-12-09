
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



import Tkinter

from STlibrary import check_color, CANVAS
from STdrawing import STtext, SToval, STline, STpolygon
import STmouse
from STimage import Image_process



class Canvas:
    """ Create a canvas widget on the right side of the frame, and handle all 
        user's code methods associated to the canvas ("canvas.xxx"). 
        Called by a redirect from the "create_frame" class which was called from 
        the user's code with the "frame.set_draw_handler" method. """
    
    def __init__(self, frame, width, height):
        """ Create a canvas on the right side of the frame """
        
        self.canvas = Tkinter.Canvas(frame, width = int(width), 
                                     height = int(height))
        self.canvas.pack(side = CANVAS["POSITION"])
        self.canvas.configure(background = check_color(CANVAS["BACKGROUND_COLOR"]))
    
    
    def new_background_color(self, color):
        """ Set a new background color for the canvas """
        self.canvas.configure(background = check_color(color))
    
    
    def set_canvas_size(self, width, height):
        """ Set a new width and height for the Canvas """
        self.canvas.config(width = int(width), height = int(height))
    
    
    def set_draw_handler(self, draw_handler):
        """ Set the default drawing handler """
        self.draw_handler = draw_handler
    
    
    def refresh_canvas(self):
        """ Refresh the Canvas widget every x milliseconds """
        self.canvas.delete('all')
        self.draw_handler(self)
        self.canvas.after(CANVAS["REFRESH_TIME"], self.refresh_canvas)
    
    
    def draw_text(self, text, position, font_size, font_color):
        """ Call the text class to add a text item on the canvas """
        font_color = check_color(font_color)
        STtext.text(self.canvas, text, position, font_size, font_color)
    
    
    def draw_circle(self, center, radius, line_width, line_color, fill_color=""):
        """ Call the oval class to add a circle/oval item on the canvas """
        line_color, fill_color = check_color(line_color), check_color(fill_color)
        SToval.oval(self.canvas, center, radius, line_width, line_color, fill_color)
    
    
    def draw_line(self, point1, point2, line_width, line_color):
        """ Call the line class to add a line item on the canvas """
        line_color = check_color(line_color)
        STline.line(self.canvas, (point1, point2), line_width, line_color)
    
    
    def draw_polyline(self, points, line_width, line_color):
        """ Call the line class to add a polyline item on the canvas """
        line_color = check_color(line_color)
        STline.line(self.canvas, points, line_width, line_color)
    
    
    def draw_polygon(self, points, line_width, line_color, fill_color = ""):
        """ Call the polygon class to add a polygon item on the canvas """
        line_color, fill_color = check_color(line_color), check_color(fill_color)
        STpolygon.polygon(self.canvas, points, line_width, line_color, fill_color)
    
    
    def draw_image(self, image, src_coor, src_size, dest_coor, dest_size, angle = 0):
        """ Process an image by calling the Image_process class and draw it """
        img = Image_process.update(image, src_coor, src_size, dest_size, angle)
        self.canvas.create_image(dest_coor, image=img)
    
    
    def set_mouseclick_handler(self, mouse_handler):
        """ Call the mouse class when a left-click mouse event occurs """
        STmouse.Mouse(self.canvas, '<Button-1>', mouse_handler)
    
    
    def set_mousedrag_handler(self, mouse_handler):
        """ Call the mouse class when a drag mouse event occurs """
        STmouse.Mouse(self.canvas, '<B1-Motion>', mouse_handler)

