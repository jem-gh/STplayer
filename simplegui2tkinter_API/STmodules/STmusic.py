
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



try:
    import pygame
    pygame.mixer.init()
except ImportError:
    print "pygame not found"

from STlibrary import SOUND



class Music:
    """ Create a Sound object using the pygame library. 
        Can Play, Stop, Set Volume at anytime. """
    
    def __init__(self, music):
        self.music = pygame.mixer.Sound(music)
        self.music.set_volume( SOUND["VOLUME"] )
        self.is_playing = False
        
        # keep track if sound.pause() has already been used once
        self.is_pause_used = False
    
    
    def play(self):
        if not self.is_playing:
            self.is_playing = True
            self.music.play()
    
    
    def pause(self):
        # will print the statement only once
        if not self.is_pause_used:
            self.is_pause_used = True
            print "sound.pause() not implemented yet... sound.rewind() has been called instead"
        self.music.stop()
    
    
    def rewind(self):
        self.is_playing = False
        self.music.stop()
    
    
    def set_volume(self, volume):
        volume = 1.0 if volume > 1.0 else volume
        volume = 0.0 if volume < 0.0 else volume
        self.music.set_volume(volume)


