
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



from threading import Thread, enumerate
from time import sleep



class Timer:
    """ Create and control (start/stop) a timer which will execute repeatedly a 
        function at a given interval of time """

    def __init__(self, interval, function):
        
        self.interval = interval / 1000.0       # from milliseconds to seconds
        self.function = function
        
        self.is_running = False
        
        self.is_last_thread = False
    
    
    def run_timer(self):
        # verify if the timer is initiated as the last thread of the main program
        self.is_last_thread = not enumerate()[0].is_alive()
        
        # keep the timer running (1) until the "stop" method is called, or (2) 
        # as long as the main application is running, or (3) forever in case of 
        # a "last_thread" timer 
        while self.is_running and (enumerate()[0].is_alive() or self.is_last_thread):
            self.function()
            sleep(self.interval)
    
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.timer = Thread(target = self.run_timer)
            self.timer.start()
    
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            self.timer.join()

