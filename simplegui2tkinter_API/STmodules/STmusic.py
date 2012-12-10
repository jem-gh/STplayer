
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



try:
    import pygame
    pygame.mixer.init()
except ImportError:
    print "pygame not found"

from STlibrary import SOUND



# keep track of the current channel id available for a music/sound
channel_id = 0



class Music:
    """ Create a Sound object using the pygame library. 
        Can Play, Pause, Stop and Set Volume """
    
    def __init__(self, music):
        global channel_id
        
        self.music = pygame.mixer.Sound(music)
        self.is_using_channel = True
        self.is_pause = False
        
        # if available, assign a channel to the sound/music or set fallback mode
        try:
            self.channel = pygame.mixer.Channel( channel_id )
            channel_id += 1
        except IndexError:
            self.is_using_channel = False
            print "Too many musics/sounds, no more available channel: fallback mode"
        
        # set sound/music volume to default volume
        self.set_volume( SOUND["VOLUME"] )
    
    
    def play(self):
        """ start playing the sound or music in current channel if it's already 
            not playing, or unpause if it was paused """
        
        if self.is_using_channel:
            if not self.channel.get_sound() and not self.is_pause:
                self.channel.play(self.music)
            elif self.is_pause:
                self.is_pause = False
                self.channel.unpause()
        
        # fallback mode if no channel was available
        if not self.is_using_channel:
            self.music.play()
    
    
    def pause(self):
        if self.is_using_channel:
            self.is_pause = True
            self.channel.pause()
        
        # fallback mode if no channel was available
        if not self.is_using_channel:
            print "pause not available in fallback mode "
    
    
    def rewind(self):
        if self.is_using_channel:
            self.channel.stop()
        
        # fallback mode if no channel was available
        if not self.is_using_channel:
            self.music.stop()
    
    
    def set_volume(self, volume):
        volume = 1.0 if volume > 1.0 else volume
        volume = 0.0 if volume < 0.0 else volume
        
        if self.is_using_channel:
            self.channel.set_volume( volume )
        
        # fallback mode if no channel was available
        if not self.is_using_channel:
            self.music.set_volume( volume )

