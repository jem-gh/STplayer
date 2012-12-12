
# STplayer (aka STconverter 2) is under the MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STplayer

###############################################################################
# STplayer (aka STconverter 2) allows you to execute Python scripts written for 
# SimpleGUI on a machine configured with Tkinter GUI instead. 
# 
# STplayer is the successor of STconverter, and is different in such ways that 
# it has been entirely rewritten to handle with a totally different approach 
# the "conversion". 
# While STconverter was converting (by this, meaning rewriting) each SimpleGUI 
# operation in the user code before the program is executed with Tkinter, 
# STplayer is an API between SimpleGUI operations and Tkinter. 
# 
# "Tkinter is Python's de-facto standard GUI (Graphical User Interface) package"
# (http://wiki.python.org/moin/TkInter)
# "SimpleGUI is a custom Python graphical user interface (GUI) module implemented 
# directly in CodeSkulptor that provides an easy to learn interface for building 
# interactive programs in Python" (http://www.codeskulptor.org) used for the 
# online Coursera course "An Introduction to Interactive Programming in Python" 
# by Joe Warren, Scott Rixner, John Greiner, and Stephen Wong (Rice University) 
# 
# I want to thank Amin Guzman for his valuable comments and suggestions on how 
# to improve STconverter, which lead to the development of STplayer
# 
# For the latest version of STplayer visit the repository on Github: 
# https://github.com/jem-gh/STplayer
# 
# STplayer is developed by Jean-Etienne Morlighem (https://github.com/jem-gh)
###############################################################################



import urllib

from STmodules import STframe, STtimer, STimage, STmusic
from STmodules.STlibrary import KEY_MAP



def create_frame(title, canvas_width, canvas_height, control_width = 200):
    """ Called from the user's code with the "simplegui.create_frame" method. """
    return STframe.Frame(title, canvas_width, canvas_height, control_width = 200)



def create_timer(interval, timer_handler):
    """ Called from the user's code with the "simplegui.create_timer" method. """
    return STtimer.Timer(interval, timer_handler)



def load_image(link):
    """ Called from the user's code with the "simplegui.load_image" method. """
    image = urllib.urlretrieve( link )[0]
    return STimage.Image_process(image)



def load_sound(link):
    """ Called from the user's code with the "simplegui.load_sound" method. """
    music = urllib.urlretrieve( link )[0]
    return STmusic.Music(music)


