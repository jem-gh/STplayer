
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



from STlibrary import KEY_MAP



class Key:
    """ Retrieve associated key value when a key is pressed or released and 
        return the value to the key handler """
    
    def __init__(self, target, mode, key_handler):
        self.key_handler = key_handler
        target.bind(mode, self.call_handler)
    
    def call_handler(self, key):
        """ Return the key value to the key handler """
        key = key.keysym.lower() if len(key.keysym) > 1 else key.keysym
        self.key_handler(KEY_MAP[key])


