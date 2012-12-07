
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



from threading import Thread, enumerate
from time import sleep



class Timer:
    """ Create and control (start/stop) a timer which will execute repeatedly a 
        function at a given interval of time """

    def __init__(self, interval, function):
        
        self.interval = interval / 1000.0
        self.function = function
        
        self.is_running = False
    
    
    def run_timer(self):
        while self.is_running and enumerate()[0].is_alive():
            self.function()
            sleep(self.interval)
    
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            self.timer = Thread(target = self.run_timer)
            self.timer.start()
    
    
    def stop(self):
        self.running = False
        self.timer.join()







