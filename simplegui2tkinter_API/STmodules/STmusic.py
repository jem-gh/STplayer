
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



try:
    import pygame
    pygame.mixer.init()
except ImportError:
    print "pygame not found"



class Music:
    """ Create a Sound object using the pygame library. 
        Can Play, Stop, Set Volume at anytime. """
    
    def __init__(self, music):
        self.music = pygame.mixer.Sound(music)
        self.music.set_volume( 1.0 )
        self.is_playing = False
    
    
    def play(self):
        if not self.is_playing:
            self.is_playing = True
            self.music.play()
    
    
    def pause(self):
        print "sound.pause() not implemented yet"
    
    
    def rewind(self):
        self.music.stop()
    
    
    def set_volume(self, volume):
        volume = 1.0 if volume > 1.0 else volume
        volume = 0.0 if volume < 0.0 else volume
        self.music.set_volume(volume)


