
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
# I want to thank Amin Guzman for his comments and suggestions on how to improve 
# STconverter, which lead to the development of STconverter 2
# 
# For the latest version of STConverter 2 visit the repository on Github: 
# https://github.com/jem-gh/STconverter-2
# 
# STconverter 2 is developed by Jean-Etienne Morlighem
###############################################################################



import Tkinter



# Adjust the Canvas refresh rate
CANVAS_REFRESH_RATE = 17 # in ms (66ms~15fps; 33ms~30fps; 17ms~60fps)

# Canvas background default color
CANVAS_BACKGROUND = "Black"

# SimpleGUI and  Tkinter use different units for Buttons and Inputs
# adjust Button and Input size ratio
BUTTON_SIZE_RATIO = 0.09
INPUT_SIZE_RATIO = 0.12



class __init__:
    """ Initialize the root window the first time simplegui2tkinter is called """
    window_root = Tkinter.Tk()



class create_frame(__init__):
    """ Set the root window title, create a frame widget, and handle all user's 
        code methods associated to the frame ("frame.xxx"). 
        Called from the user's code with the "simplegui.create_frame" method. 
        A canvas widget is created only if required by using the method 
        "frame.set_draw_handler". """
    
    def __init__(self, title, canvas_width, canvas_height, control_width = 200):
        """ Set the root window title and create the frame widget """
        
        # set the root window title
        self.window_root.title(title)
        
        # create the frame
        self.frame = Tkinter.Frame(self.window_root)
        self.frame.pack()
        
        # variables used by other methods
        self.canvas_width = canvas_width            # by canvas
        self.canvas_height = canvas_height          # by canvas
        self.canvas_background = CANVAS_BACKGROUND  # by canvas
        self.control_width = control_width          # by label, button, input
    
    
    def start(self):
        """ Initiate the loop event of the root window """
        self.window_root.mainloop()
    
    
    def set_draw_handler(self, draw_handler):
        """ Create the canvas widget by calling the ST_canvas class. 
            Call the canvas methods to set the drawing handler and to refresh 
            the drawing. """
        
        # create the canvas
        self.canvas = ST_canvas(self.frame, self.canvas_width, 
                                self.canvas_height, self.canvas_background)
        
        # call the canvas method to set the canvas drawing handler
        self.canvas.set_draw_handler(draw_handler)
        
        # create and start the refresh process of the canvas
        refresh = STconverter_timer(self.window_root, CANVAS_REFRESH_RATE, 
                                    self.canvas.refresh_canvas)
        refresh.set_status(True)
    
    
    def set_canvas_background(self, color):
        """ Call the canvas method to set a new background """
        try:
            self.canvas.new_background_color(color)
        except AttributeError:
            self.canvas_background = color
    
    
    def add_label(self, text):
        """ Call the label class to add a label on the frame """
        
        return Frame_label(self.frame, text, self.control_width)
    
    
    def add_button(self, text, button_handler, width = 0):
        """ Call the button class to add a button on the frame """
        
        # adjust the width if its larger than the expected control width 
        width = self.control_width if self.control_width < width else width
        
        Frame_button(self.frame, text, button_handler, width)
    
    
    def add_input(self, text, input_handler, width):
        """ Call the input and label classes to add an input on the frame and 
            its corresponding label """
        
        # adjust the width if its larger than the expected control width 
        width = self.control_width if self.control_width < width else width
        
        Frame_label(self.frame, text, self.control_width)
        Frame_input(self.frame, input_handler, width)
    
    
    def set_keydown_handler(self, key_handler):
        """ Call the key class when a key is pressed """
        STconverter_key('<Key>', key_handler)
    
    
    def set_keyup_handler(self, key_handler):
        """ Call the key class when a key is released """
        STconverter_key('<KeyRelease>', key_handler)
    
    
    def set_mouseclick_handler(self, mouse_handler):
        """ Call the mouse class when a left-click occurs """
        STconverter_mouse('<Button-1>', mouse_handler)
    
    
    def set_mousedrag_handler(self, mouse_handler):
        pass



class create_timer(__init__):
    """ Create and control a timer with its associated handler by calling the 
        STconverter_timer class. 
        Called from the user's code with the "simplegui.create_timer" method. """
    
    def __init__(self, interval, timer_handler):
        self.t = STconverter_timer(self.window_root, interval, timer_handler)
    
    def start(self):
        self.t.set_status(True)
    
    def stop(self):
        self.t.set_status(False)



# dictionary of colors sometimes not recognized with their names and HEX values 
COLORS_PROB = {"aqua":      '#00FFFF', "Aqua":      '#00FFFF', 
               "fuchsia":   '#FF00FF', "Fuchsia":   '#FF00FF', 
               "lime":      '#00FF00', "Lime":      '#00FF00', 
               "olive":     '#808000', "Olive":     '#808000', 
               "silver":    '#C0C0C0', "Silver":    '#C0C0C0', 
               "teal":      '#008080', "Teal":      '#008080'}

def check_color(color):
    return COLORS_PROB[color] if color in COLORS_PROB else color



class ST_canvas:
    """ Create a canvas widget on the right side of the frame, and handle all 
        user's code methods associated to the canvas ("canvas.xxx"). 
        Called by a redirect from the "create_frame" class which was called from 
        the user's code with the "frame.set_draw_handler" method. """
    
    def __init__(self, frame, canvas_width, canvas_height, background_color):
        """ Create a canvas on the right side of the frame """
        
        self.canvas = Tkinter.Canvas(frame, width = int(canvas_width), 
                                     height = int(canvas_height))
        self.canvas.pack(side = 'right')
        self.canvas.configure(background = check_color(background_color))
    
    
    def new_background_color(self, color):
        """ Set a new background color for the canvas """
        self.canvas.configure(background = check_color(color))
    
    
    def set_draw_handler(self, draw_handler):
        """ Set the default drawing handler """
        self.draw_handler = draw_handler
    
    
    def refresh_canvas(self):
        """ Refresh the canvas widget """
        self.canvas.delete('all')
        self.draw_handler(self)
    
    
    def draw_text(self, text, position, font_size, font_color):
        """ Call the text class to add a text item on the canvas """
        font_color = check_color(font_color)
        Canvas_text(self.canvas, text, position, font_size, font_color)
    
    
    def draw_circle(self, center, radius, line_width, line_color, fill_color=""):
        """ Call the oval class to add a circle/oval item on the canvas """
        line_color, fill_color = check_color(line_color), check_color(fill_color)
        Canvas_oval(self.canvas, center, radius, line_width, line_color, fill_color)
    
    
    def draw_line(self, point1, point2, line_width, line_color):
        """ Call the line class to add a line item on the canvas """
        line_color = check_color(line_color)
        Canvas_line(self.canvas, (point1, point2), line_width, line_color)
    
    
    def draw_polygon(self, points, line_width, line_color, fill_color = ""):
        """ Call the polygon class to add a polygon item on the canvas """
        line_color, fill_color = check_color(line_color), check_color(fill_color)
        Canvas_polygon(self.canvas, points, line_width, line_color, fill_color)



class Frame_label:
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
    
    def __init__(self, canvas, text, position, font_size, font_color):
        
        # adjust the position of the text for the bottom-left corner being 
        # at the points position
        x, y = position
        y += int(font_size / 3)
        
        canvas.create_text([x, y], anchor='sw', text = text, fill = font_color, 
                           font = ('DejaVu Serif Condensed', font_size))



class Canvas_oval:
    """ Add an oval item on the canvas """
    
    def __init__(self, canvas, center, radius, line_width, line_color, fill_color):
        
        # go from a center-radius reference to an ellipse coordinates
        x, y = center
        coordinates = ((x - radius), (y - radius), (x + radius), (y + radius))
        
        canvas.create_oval(coordinates, width = line_width, 
                           outline = line_color, fill = fill_color)



class Canvas_line:
    """ Add a line item on the canvas """
    
    def __init__(self, canvas, points, line_width, line_color):
        canvas.create_line(points, width = line_width, fill = line_color)



class Canvas_polygon:
    """ Add a polygon item on the canvas """
    
    def __init__(self, canvas, points, line_width, line_color, fill_color):
        canvas.create_polygon(points, width = line_width, outline = line_color, 
                              fill = fill_color)



# key and key values dictionary
KEY_MAP = {"0": 48, "1": 49, "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, 
           "7": 55, "8": 56, "9": 57, "A": 65, "B": 66, "C": 67, "D": 68, 
           "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74, "K": 75, 
           "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, 
           "S": 83, "T": 84, "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, 
           "Z": 90, "a": 97, "b": 98, "c": 99, "d": 100, "e": 101, "f": 102, 
           "g": 103, "h": 104, "i": 105, "j": 106, "k": 107, "l": 108, 
           "m": 109, "n": 110, "o": 111, "p": 112, "q": 113, "r": 114, 
           "s": 115, "t": 116, "u": 117, "v": 118, "w": 119, "x": 120, 
           "y": 121, "z": 122, "BackSpace": 65288, "Tab": 65289, "Return": 65293, 
           "Pause": 65299, "Escape": 65307, "Home": 65360, "Left": 65361, 
           "Up": 65362, "Right": 65363, "Down": 65364, "Prior": 65365, 
           "Next": 65366, "End": 65367, "space": 32, "Shift_L": 65505, 
           "Shift_R": 65506, "Control_L": 65507, "Control_R": 65508, 
           "Caps_Lock": 65509, "Alt_L": 65513, "Alt_R": 65514, "Delete": 65535, 
           "tab": 65289, "return": 65293, "escape": 65307, "left": 65361, 
           "up": 65362, "right": 65363, "down": 65364, "Space": 32}



class STconverter_key(__init__):
    """ Retrieve associated key value when a key is pressed or released and 
        return the value to the key handler """
    
    def __init__(self, mode, key_handler):
        self.key_handler = key_handler
        self.window_root.bind(mode, self.call_handler)
    
    def call_handler(self, key):
        """ Return the key value to the key handler """
        self.key_handler( KEY_MAP[key.keysym] )



class STconverter_mouse(__init__):
    """ Retrieve the mouse coordinate during a mouse event (click or drag) """
    
    def __init__(self, mode, mouse_handler):
        self.mouse_handler = mouse_handler
        self.window_root.bind(mode, self.call_handler)
        
    def call_handler(self, coordinate):
        """ Return the coordinate of the mouse """
        self.mouse_handler( (coordinate.x, coordinate.y) )



class STconverter_timer:
    """ Create a timer which will execute repeatedly a function at a given 
        interval of time """
    
    def __init__(self, instance_root, interval, function):
        self.instance_root = instance_root
        self.interval = int(interval)
        self.function = function
        self.status = False
    
    def set_status(self, status):
        if status != self.status:
            self.status = status
            self.run()
    
    def run(self):
        if self.status:
            self.instance_root.after(self.interval, self.run)
            self.function()






