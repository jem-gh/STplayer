
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


from os import path
import Tkinter, tkFileDialog



# text in Labels and Buttons
l_intro = "STconverter 2 allows you to execute Python scripts written for "\
        "SimpleGUI on a machine configured with Tkinter GUI instead. "

l_info = "REMEMBER:\n\n"\
       "- 'import simplegui'  has to be replaced with:\n"\
       "  'from simplegui2tkinter_API import simplegui2tkinter as simplegui'\n\n"\
       "- 'frame.start()'  has to be the last line of your code"

b_open = "Select a file containing your SimpleGUI code"

b_run = "Run!"
l_run = "(loading the program can take few seconds... "\
        "this window will close during loading)"

l_author = "developped by  Jean-Etienne Morlighem"
l_contact = "https://github.com/jem-gh"



class Main:
    def __init__(self):
        
        self.window_root = Tkinter.Tk()
        self.window_root.title("SimpleGUI/Tkinter converter '2'")
        
        self.frame = Tkinter.Frame(self.window_root, padx=10, pady=10)
        self.frame.grid()
        
        self.interface()
        
        self.window_root.mainloop()
    
    
    def interface(self):
        """ draw all parts of the GUI """
        
        # block the resizing of the GUI 
        self.window_root.resizable(0, 0)
        
        # title
        label_title = Tkinter.Label(self.frame, text="STconverter '2'", 
                              font=("Serif", 18, "bold italic"), 
                              foreground="#0000A3")
        label_title.grid(row=0, columnspan=3)
        
        # intro
        label_intro = Tkinter.Label(self.frame, text=l_intro, padx=20, pady=20)
        label_intro.grid(row=1, columnspan=3)
        
        # information
        label_info = Tkinter.Label(self.frame, text=l_info, justify="left", 
                             font=("Courier", 10), background="#E8E8E8", 
                             borderwidth=1, relief="sunken", padx=20, pady=10)
        label_info.grid(row=2, columnspan=3)
        
        # load a file
        self.frame.rowconfigure(3, minsize=60)
        button_open = Tkinter.Button(self.frame, text=b_open, width=40, pady=5, 
                              font=("Serif", 10, "bold"), command=self.file_open)
        button_open.grid(row=3, columnspan=3, sticky="S")
        
        self.frame.rowconfigure(4, minsize=60)
        self.file_name = Tkinter.StringVar()
        self.label_file = Tkinter.Label(self.frame, textvariable=self.file_name)
        self.label_file.grid(row=4, columnspan=3)
        
        # run
        self.button_run = Tkinter.Button(self.frame, text=b_run, width=40, 
                                  font=("Serif", 10, "bold"), state="disabled", 
                                  command=self.run_code)
        self.button_run.grid(row=5, columnspan=3)
        
        self.frame.rowconfigure(6, minsize=50)
        label_run = Tkinter.Label(self.frame, text=l_run)
        label_run.grid(row=6, columnspan=3, sticky="N")
        
        # About and Quit
        self.about_state = False
        
        button_about = Tkinter.Button(self.frame, text="About", width=10, 
                                      command=self.change_about_state)
        button_about.grid(row=7, column=0, rowspan=2)
        
        self.frame.rowconfigure(7, minsize=30)
        self.label_author = Tkinter.Label(self.frame, state = "disabled", 
                                    text=l_author, font=("Serif", 10, "italic"), 
                                    foreground="#0000A3", 
                                    disabledforeground="#D8D8D8")
        self.label_author.grid(row=7, column=1, sticky="S")
        
        self.frame.rowconfigure(8, minsize=30)
        self.label_contact = Tkinter.Label(self.frame, state = "disabled", 
                                     text=l_contact, disabledforeground="#D8D8D8")
        self.label_contact.grid(row=8, column=1, sticky="N")
        
        button_quit = Tkinter.Button(self.frame, text="Quit", width=10, 
                                     command=quit)
        button_quit.grid(row=7, column=2, rowspan=2)
        
    
    
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
            self.input_data = input_loaded.read()
            self.input_path = input_loaded.name
            input_loaded.close()
            
            name = path.split(self.input_path)[1]
            
            self.file_name.set(name)
            self.button_run.configure(text="Run "+name+" !", state="normal")
    
    
    def run_code(self):
        """ Close current window and execute the SimpleGUI code """
        self.window_root.destroy()
        execfile(self.input_path, {})



