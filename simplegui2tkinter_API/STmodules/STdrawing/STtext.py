
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



class Text:
    """ Add a text item on the canvas """
    
    def __init__(self, canvas, text, position, font_size, font_color):
        
        # adjust the position of the text for the bottom-left corner being 
        # at the points position
        x, y = position
        y += int(font_size / 3)
        
        canvas.create_text([x, y], anchor='sw', text = text, fill = font_color, 
                           font = ('DejaVu Serif Condensed', font_size))



