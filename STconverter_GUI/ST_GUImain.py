
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
# I want to thank Amin Guzman for his valuable comments and suggestions on how 
# to improve STconverter, which lead to the development of STconverter 2
# 
# For the latest version of STConverter 2 visit the repository on Github: 
# https://github.com/jem-gh/STconverter-2
# 
# STconverter 2 is developed by Jean-Etienne Morlighem
###############################################################################



import Tkinter, tkFileDialog



class Main:
    def __init__(self):
        
        self.window_root2 = Tkinter.Tk()
        self.window_root2.title("SimpleGUI/Tkinter converter '2'")
        
        self.frame2 = Tkinter.Frame(self.window_root2)
        self.frame2.grid()
        
        self.interface()
        
        self.window_root2.mainloop()
    
    
    def interface(self):
        """ """
        
        label_open = Tkinter.Label(self.frame2, text="In development")
        label_open.grid()
        
        button_open = Tkinter.Button(self.frame2, text="Select file", command=self.file_open)
        button_open.grid()
        
        self.text_code = Tkinter.Text(self.frame2)
        self.text_code.grid()
        
        button_run = Tkinter.Button(self.frame2, text="Run", command=self.run_code)
        button_run.grid()
    
    
    
    def file_open(self):
        """  """
        
        input_loaded = tkFileDialog.askopenfile(title="Choose a file to convert")
        
        if input_loaded:
            self.input_data = input_loaded.read()
            self.input_path = input_loaded.name
            input_loaded.close()
            self.text_code.insert("insert", self.input_data)
    
    
    def run_code(self):
        """ """
        self.window_root2.destroy()
        execfile(self.input_path, {})



