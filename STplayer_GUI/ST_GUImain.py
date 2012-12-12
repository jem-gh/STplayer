
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


from os import path
import Tkinter, tkFileDialog

from ST_GUItext import TEXT



class Main:
    def __init__(self):
        
        self.window_root = Tkinter.Tk()
        self.window_root.title(TEXT["window_title"])
        
        self.frame = Tkinter.Frame(self.window_root, padx=10, pady=10)
        self.frame.grid()
        
        self.interface()
        
        self.window_root.mainloop()
    
    
    def interface(self):
        """ draw all parts of the GUI """
        
        # block the resizing of the GUI 
        self.window_root.resizable(0, 0)
        
        # title
        label_title = Tkinter.Label(self.frame, text=TEXT["l_title"], 
                              font=("Serif", 18, "bold italic"), 
                              foreground=TEXT["COLOR_TITLE"])
        label_title.grid(row=0, columnspan=3)
        
        # intro
        label_intro = Tkinter.Label(self.frame, text=TEXT["l_intro"], 
                                    padx=20, pady=20)
        label_intro.grid(row=1, columnspan=3)
        
        # information
        label_info = Tkinter.Label(self.frame, text=TEXT["l_info"], padx=20, 
                             pady=10, justify="left", font=("Courier", 10), 
                             background="#E8E8E8", borderwidth=1, relief="sunken")
        label_info.grid(row=2, columnspan=3)
        
        # load a file
        self.frame.rowconfigure(3, minsize=60)
        button_open = Tkinter.Button(self.frame, text=TEXT["b_open"], width=40, 
                              font=("Serif", 10, "bold"), command=self.file_open)
        button_open.grid(row=3, columnspan=3, sticky="S")
        
        # label for code on software verification
        self.frame.rowconfigure(4, minsize=40)
        self.file_OK = Tkinter.StringVar()
        self.label_file_OK = Tkinter.Label(self.frame, textvariable=self.file_OK, 
                                           font=("Serif", 11, "bold"))
        self.label_file_OK.grid(row=4, columnspan=3, sticky="S")
        
        self.PIL_OK = Tkinter.StringVar()
        self.label_PIL_OK = Tkinter.Label(self.frame, textvariable=self.PIL_OK, 
                                           font=("Serif", 11, "bold"), pady=5)
        self.label_PIL_OK.grid(row=5, columnspan=3)
        
        self.frame.rowconfigure(6, minsize=40)
        self.pygame_OK = Tkinter.StringVar()
        self.label_pygame_OK = Tkinter.Label(self.frame, 
                                             textvariable=self.pygame_OK, 
                                             font=("Serif", 11, "bold"))
        self.label_pygame_OK.grid(row=6, columnspan=3, sticky="N")
        
        # run
        self.button_run = Tkinter.Button(self.frame, text=TEXT["b_run"], 
                                  width=40, font=("Serif", 10, "bold"), 
                                  state="disabled", command=self.run_code)
        self.button_run.grid(row=7, columnspan=3)
        
        self.frame.rowconfigure(8, minsize=50)
        label_run = Tkinter.Label(self.frame, text=TEXT["l_run"])
        label_run.grid(row=8, columnspan=3, sticky="N")
        
        # About and Quit
        self.about_state = False
        
        button_about = Tkinter.Button(self.frame, text="About", width=10, 
                                      command=self.change_about_state)
        button_about.grid(row=9, column=0, rowspan=2)
        
        self.frame.rowconfigure(9, minsize=30)
        self.label_author = Tkinter.Label(self.frame, state = "disabled", 
                                    text=TEXT["l_author"], foreground="#0000A3", 
                                    font=("Serif", 10, "italic"), 
                                    disabledforeground="#D8D8D8")
        self.label_author.grid(row=9, column=1, sticky="S")
        
        self.frame.rowconfigure(10, minsize=30)
        self.label_contact = Tkinter.Label(self.frame, text=TEXT["l_contact"], 
                                     state = "disabled", 
                                     disabledforeground="#D8D8D8")
        self.label_contact.grid(row=10, column=1, sticky="N")
        
        button_quit = Tkinter.Button(self.frame, text="Quit", width=10, 
                                     command=quit)
        button_quit.grid(row=9, column=2, rowspan=2)
    
    
    def change_about_state(self):
        """ change About-associated label' state from Normal to Disable """
        
        if not self.about_state:
            self.about_state = True
            self.label_author.config(state = "normal")
            self.label_contact.config(state = "normal")
        
        elif self.about_state:
            self.about_state = False
            self.label_author.config(state = "disabled")
            self.label_contact.config(state = "disabled")
    
    
    def file_open(self):
        """ Open and load a file """
        
        input_loaded = tkFileDialog.askopenfile(title="Choose a file to convert")
        
        if input_loaded:
            self.input_path = input_loaded.name
            input_loaded.close()
            
            # disable the Run button and reset all information labels until the 
            # file is totally verified
            self.button_run.configure(text=TEXT["b_run"], state="disabled")
            self.file_OK.set("")
            self.PIL_OK.set("")
            self.pygame_OK.set("")
            
            # start checking the file
            self.prepare_data()
    
    
    def prepare_data(self):
        """ Verify the code and test if required module are installed """
        
        with open(self.input_path, 'r') as self.file:
            
            name = path.split(self.input_path)[1]
            content = self.file.read()
            
            is_code_OK = True
            
            # verify if the file seems legit to be SimpleGUI code
            if "simplegui" not in content:
                self.file_OK.set(name + TEXT["l_file_OK_e"])
                self.label_file_OK.configure(
                                   foreground=TEXT["COLOR_ERROR"])
                self.file.close()
                return
            else:
                self.file_OK.set(name + TEXT["l_file_OK_g"])
                self.label_file_OK.configure(
                                   foreground=TEXT["COLOR_CORRECT"])
            
            # if images are used, check if PIL is installed 
            if "simplegui.load_image" in content:
                try:
                    from PIL import Image, ImageTk
                    self.PIL_OK.set(TEXT["l_PIL_OK_g"])
                    self.label_PIL_OK.configure(
                                      foreground=TEXT["COLOR_CORRECT"])
                except ImportError:
                    self.PIL_OK.set(TEXT["l_PIL_OK_e"])
                    self.label_PIL_OK.configure(
                                      foreground=TEXT["COLOR_ERROR"])
                    is_code_OK = False
                    self.file.close()
            
            # if sounds/musics are used, check if pygame is installed 
            if "simplegui.load_sound" in content:
                try:
                    import pygame
                    self.pygame_OK.set(TEXT["l_pygame_OK_g"])
                    self.label_pygame_OK.configure(
                                         foreground=TEXT["COLOR_CORRECT"])
                    if "mp3" in content or "MP3" in content:
                        self.pygame_OK.set(TEXT["l_pygame_OK_e2"])
                        self.label_pygame_OK.configure(
                                             foreground=TEXT["COLOR_ERROR"])
                except ImportError:
                    self.pygame_OK.set(TEXT["l_pygame_OK_e1"])
                    self.label_pygame_OK.configure(
                                         foreground=TEXT["COLOR_ERROR"])
                    is_code_OK = False
                    self.file.close()

            # if no error arises during the verification, activate Run button
            if is_code_OK:
                self.button_run.configure(text="Run "+name+" !", state="normal")
    
    
    def run_code(self):
        """ Close current window and execute the SimpleGUI code """
        self.window_root.destroy()
        execfile(self.input_path, {})
        self.file.close()


