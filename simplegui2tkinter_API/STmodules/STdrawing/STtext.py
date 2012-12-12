
# STplayer (aka STconverter 2) is under the MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STplayer



def text(canvas, text, position, font_size, font_color):
    """ Add a text item on the canvas """
    
    # adjust the position of the text for the bottom-left corner being 
    # at the position coordinate 
    x, y = position
    y += int(font_size / 3)
    
    canvas.create_text([x, y], anchor='sw', text = text, fill = font_color, 
                       font = ('DejaVu Serif Condensed', int(font_size)))


