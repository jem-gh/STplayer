#!/usr/bin/python

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



import sys

from STplayer_GUI import ST_GUImain
from simplegui2tkinter_API import simplegui2tkinter
sys.modules['simplegui'] = simplegui2tkinter



if __name__ == "__main__":
    
    print "STplayer started!"
    
    try:
        # when running STplayer in command line, start executing the 
        # SimpleGUI program if given as argument
        
        file_simplegui = sys.argv[1]
        print "SimpleGUI program is loading... Thanks for your patience!"
        execfile( file_simplegui, {} )
    
    
    except IndexError:
        # when launching STplayer in GUI mode or from command line without 
        # providing a SimpleGUI program, start the GUI
        
        print "STplayer GUI initializing!"
        ST_GUImain.Main()

