
# MIT License
# Copyright (c) 2012 Jean-Etienne Morlighem <jem.nvnt@gmail.com>
# https://github.com/jem-gh/STconverter-2



# SUPPORT LIBRARIES



CANVAS = {
    # Canvas background default color
    "BACKGROUND_COLOR": "Black", 
    # Adjust the Canvas refresh time in ms (66ms~15fps; 33ms~30fps; 17ms~60fps)
    "REFRESH_TIME": 17, 
}



WIDGET = {
    # SimpleGUI and Tkinter use different units for Button and Input
    "BUTTON_SIZE_RATIO": 0.09, 
    "INPUT_SIZE_RATIO" : 0.12,
}



# name of colors sometimes not recognized with their HEX values 
COLORS_PROB = {
    "aqua":      '#00FFFF', 
    "fuchsia":   '#FF00FF', 
    "lime":      '#00FF00', 
    "olive":     '#808000', 
    "silver":    '#C0C0C0', 
    "teal":      '#008080', 
}

def check_color(color):
    color = color.lower()
    return COLORS_PROB[color] if color in COLORS_PROB else color




# key and key values dictionary
KEY_MAP = {
    "0": 48, 
    "1": 49, 
    "2": 50, 
    "3": 51, 
    "4": 52, 
    "5": 53, 
    "6": 54, 
    "7": 55, 
    "8": 56, 
    "9": 57, 
    
    "A": 65, 
    "B": 66, 
    "C": 67, 
    "D": 68, 
    "E": 69, 
    "F": 70, 
    "G": 71, 
    "H": 72, 
    "I": 73, 
    "J": 74, 
    "K": 75, 
    "L": 76, 
    "M": 77, 
    "N": 78, 
    "O": 79, 
    "P": 80, 
    "Q": 81, 
    "R": 82, 
    "S": 83, 
    "T": 84, 
    "U": 85, 
    "V": 86, 
    "W": 87, 
    "X": 88, 
    "Y": 89, 
    "Z": 90, 
    
    "a": 97, 
    "b": 98, 
    "c": 99, 
    "d": 100, 
    "e": 101, 
    "f": 102, 
    "g": 103, 
    "h": 104, 
    "i": 105, 
    "j": 106, 
    "k": 107, 
    "l": 108, 
    "m": 109, 
    "n": 110, 
    "o": 111, 
    "p": 112, 
    "q": 113, 
    "r": 114, 
    "s": 115, 
    "t": 116, 
    "u": 117, 
    "v": 118, 
    "w": 119, 
    "x": 120, 
    "y": 121, 
    "z": 122, 
    
    "left": 65361, 
    "up": 65362, 
    "right": 65363, 
    "down": 65364, 
    "space": 32, 
}



