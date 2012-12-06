
###############################################################################
# STconverter 2 allows you to execute Python scripts written for SimpleGUI on 
# a machine configured with Tkinter GUI instead. 
# 
# STconverter 2 is the successor of STconverter, and is different in such ways 
# it has been entirely rewritten to handle with a totally different approach 
# the "conversion". 
# While the first version of STconverter was converting each SimpleGUI operation 
# in the user code to be executable by Tkinter, STconverter 2 is an API between 
# SimpleGUI operations and Tkinter. 
# 
# "Tkinter is Python's de-facto standard GUI (Graphical User Interface) package"
# (http://wiki.python.org/moin/TkInter)
# "SimpleGUI is a custom Python graphical user interface (GUI) module implemented 
# directly in CodeSkulptor that provides an easy to learn interface for building 
# interactive programs in Python" (http://www.codeskulptor.org) used for the 
# online Coursera course "An Introduction to Interactive Programming in Python" 
# by Joe Warren, Scott Rixner, John Greiner, and Stephen Wong (Rice University) 
# 
# I want to thank Amín Guzmán for his comments and suggestions on how to improve 
# STconverter, which lead to the development of STconverter 2
# 
# For the latest version of STConverter 2 visit the repository on Github: 
# https://github.com/jem-gh/STconverter-2
# 
# STconverter 2 is developed by Jean-Etienne Morlighem
###############################################################################



import Tkinter



CANVAS_REFRESH_RATE = 66 # in ms (66ms~15fps; 33ms~30fps; 17ms~60fps)

BUTTON_SIZE_RATIO = 0.09
INPUT_SIZE_RATIO = 0.12



class create_frame:
    """ Initialize the root window with a frame widget, and handle all user's 
        code methods associated to the frame ("frame.xxx"). 
        Called from the user's code with the "simplegui.create_frame" method. 
        A canvas widget is created only if required by using the method 
        "frame.set_draw_handler". """
    
    def __init__(self, title, canvas_width, canvas_height, control_width = 200):
        """ initialize the root window and create the frame widget """
        
        # initiate and set the root window title
        self.window_root = Tkinter.Tk()
        self.window_root.title(title)
        
        # create the frame
        self.frame = Tkinter.Frame(self.window_root)
        self.frame.pack()
        
        # variables used by other methods
        self.canvas_width = canvas_width        # by canvas
        self.canvas_height = canvas_height      # by canvas
        self.control_width = control_width      # by label, button, input
        
    
    def start(self):
        """ Initiate the loop event of the GUI """
        self.window_root.mainloop()
    
    
    def set_draw_handler(self, draw_handler):
        """ Create the canvas widget by calling the ST_canvas class. 
            Call the canvas methods to set the drawing handler and to refresh 
            the drawing. """
        
        # create the canvas
        self.canvas = ST_canvas(self.frame, self.canvas_width, self.canvas_height)
        
        # call the canvas method to set the canvas drawing handler
        self.canvas.set_draw_handler(draw_handler)
        
        # start the refresh
        t = STconverter_timer(self.window_root, CANVAS_REFRESH_RATE, 
                              self.canvas.refresh_canvas)
        t.set_status(True)
    
    
    def set_canvas_background(self, color):
        """ Call the canvas method to set a new background """
        self.canvas.new_background_color(color)
    
    
    def add_button(self, text, button_handler, width = 0):
        """ Call the button class to add a button on the frame """
        
        # adjust the control width in case the button is larger 
        if self.control_width < width:
            self.control_width = width
        
        Frame_button(self.frame, text, button_handler, width)
    
    
    def add_input(self, text, input_handler, width):
        """ Call the input and label classed to add an input on the frame and 
            its corresponding label """
        
        # adjust the control width in case the input is larger 
        if self.control_width < width:
            self.control_width = width
        
        label_width = self.control_width if self.control_width > width else width
        
        Frame_label(self.frame, text, label_width)
        Frame_input(self.frame, input_handler, width)



class ST_canvas:
    """ Create a canvas widget on the right side of the frame, and handle all 
        user's code methods associated to the canvas ("canvas.xxx"). 
        Called by a redirect from the "create_frame" class which was called from 
        the user's code with the "frame.set_draw_handler" method. """
    
    def __init__(self, frame, canvas_width, canvas_height):
        """ Create a canvas on the right side of the frame with a default black 
            background """
        
        self.canvas = Tkinter.Canvas(frame, width = int(canvas_width), 
                                     height = int(canvas_height))
        self.canvas.pack(side='right')
        self.canvas.configure(background = "Black")
    
    
    def new_background_color(self, color):
        """ Set a new background color for the canvas """
        self.canvas.configure(background = color)
    
    
    def set_draw_handler(self, draw_handler):
        """ Set the default drawing handler """
        self.draw_handler = draw_handler
    
    
    def refresh_canvas(self):
        """ Refresh the canvas widget """
        self.canvas.delete('all')
        self.draw_handler(self)
    
    
    def draw_text(self, text, point, font_size, font_color):
        """ Call the text class to add a text item on the canvas """
        Canvas_text(self.canvas, text, point, font_size, font_color)
    
    
    def draw_circle(self, center_point, radius, line_width, line_color, fill_color=""):
        """ Call the oval class to add a circle/oval item on the canvas """
        Canvas_oval(self.canvas, center_point, radius, line_width, line_color, fill_color)
    
    
    def draw_line(self, point1, point2, line_width, line_color):
        """ Call the line class to add a line item on the canvas """
        Canvas_line(self.canvas, (point1, point2), line_width, line_color)
    
    
    def draw_polygon(self, point_list, line_width, line_color, fill_color = ""):
        """ Call the polygon class to add a polygon item on the canvas """
        Canvas_polygon(self.canvas, point_list, line_width, line_color, fill_color)



class Frame_label:
    """ Add a label widget on the left side of the frame """
    
    def __init__(self, frame, text, width):
        self = Tkinter.Label(frame, text = text, wraplength = width)
        self.pack()



class Frame_button:
    """ Add a button widget on the left side of the frame """
    
    def __init__(self, frame, text, button_handler, width):
        self = Tkinter.Button(frame, text = text, command = button_handler)
        self.config(width = int(width * BUTTON_SIZE_RATIO))
        self.pack()



class Frame_input:
    """ Add an input widget on the left side of the frame """
    
    def __init__(self, frame, input_handler, width):
        
        self.input_handler = input_handler
        
        self.input = Tkinter.Entry(frame)
        self.input.bind('<Return>', self.call_handler)
        self.input.config(width = int(width * INPUT_SIZE_RATIO))
        self.input.pack()
    
    def call_handler(self, input_value):
        """ Return the value entered in the input to the input handler """
        
        self.input_handler(self.input.get())



class Canvas_text:
    """ Add a text item on the canvas """
    
    def __init__(self, canvas, text, point, font_size, font_color):
        
        # adjust the position of the text for the bottom-left corner being 
        # at the points position
        x, y = point
        y += int(font_size / 3)
        
        canvas.create_text([x, y], anchor='sw', text = text, fill = font_color, 
                           font = ('DejaVu Serif Condensed', font_size))



class Canvas_oval:
    """ Add an oval item on the canvas """
    
    def __init__(self, canvas, center_point, radius, line_width, line_color, fill_color):
        
        # go from a center-radius reference to an ellipse coordinates
        x, y = center_point
        coordinates = ((x - radius), (y - radius), (x + radius), (y + radius))
        
        canvas.create_oval(coordinates, width = line_width, 
                           outline = line_color, fill = fill_color)



class Canvas_line:
    """ Add a line item on the canvas """
    
    def __init__(self, canvas, points, line_width, line_color):
        canvas.create_line(points, width = line_width, fill = line_color)



class Canvas_polygon:
    """ Add a polygon item on the canvas """
    
    def __init__(self, canvas, point_list, line_width, line_color, fill_color):
        canvas.create_polygon(point_list, width = line_width, 
                              outline = line_color, fill = fill_color)



class STconverter_timer:
    """ Create a timer which will execute repeatedly a function at a given 
        interval of time """
    
    def __init__(self, root, interval, function):
        self.root = root
        self.interval = int(interval)
        self.function = function
        self.status = False
    
    def set_status(self, status):
        if status != self.status:
            self.status = status
            self.run()
    
    def run(self):
        if self.status:
            self.root.after(self.interval, self.run)
            self.function()






