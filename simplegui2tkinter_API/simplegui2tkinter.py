
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2

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



import urllib

try:
    from PIL import Image
except ImportError:
    print "Python Imaging Library not found"

from STmodules import STframe, STtimer, STimage
from STmodules.STlibrary import KEY_MAP



def create_frame(title, canvas_width, canvas_height, control_width = 200):
    """ Called from the user's code with the "simplegui.create_frame" method. """
    return STframe.Frame(title, canvas_width, canvas_height, control_width = 200)



def create_timer(interval, timer_handler):
    """ Called from the user's code with the "simplegui.create_timer" method. """
    return STtimer.Timer(interval, timer_handler)



def load_image(link):
    """ Called from the user's code with the "simplegui.load_image" method. """
    image = Image.open(urllib.urlretrieve( link )[0])
    return STimage.Image_process(image)



def load_sound():
    pass






