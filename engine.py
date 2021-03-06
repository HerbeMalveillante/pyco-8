import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import platform
from termcolor import cprint
import unicodedata
from config import RESOLUTION, ICON, COLORS, INPUT, FONT, WELCOME
import math


FPS = 30
NAME = "pyco-8 game"
SCREEN = None
FRAME = 0
gameclock = pygame.time.Clock()

KEYPRESSEVENTS = {}

for key in INPUT.keys():
    KEYPRESSEVENTS[key] = 0

### LOG ###
def info(arg):
    cprint(f"[INFO] - {arg}", 'blue')
def error(arg):
    cprint(f"[ERROR] - {arg}", 'red')
def warning(arg):
    cprint(f"[WARNING] - {arg}", 'yellow')
def debug(arg):
    cprint(f"[DEBUG] - {arg}", 'white')
def success(arg):
    cprint(f"[SUCCESS] - {arg}", 'green')


def run(init, update, draw):
    global SCREEN
    global KEYPRESSEVENTS
    global FRAME
    pygame.init()
    SCREEN = pygame.display.set_mode(RESOLUTION, flags=pygame.SCALED|pygame.RESIZABLE)
    logo = pygame.image.load(ICON)
    pygame.display.set_icon(logo)
    pygame.display.set_caption(NAME)
    if init is not None:
        init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # each key has three possible values : 
        # -> 0 : not pressed
        # -> 1 : just got pressed
        # -> 2 : held down
        # -> 3 : just got released

        for key in KEYPRESSEVENTS.keys():
            if KEYPRESSEVENTS[key] == 1:
                KEYPRESSEVENTS[key] = 2
            elif KEYPRESSEVENTS[key] == 3:
                KEYPRESSEVENTS[key] = 0
            
            if btn(key) and KEYPRESSEVENTS[key] == 0:
                KEYPRESSEVENTS[key] = 1
            elif not btn(key) and KEYPRESSEVENTS[key] == 2:
                KEYPRESSEVENTS[key] = 3
        
        if update is not None:
            update()
        if draw is not None:
            draw()
        pygame.display.flip()
        gameclock.tick(FPS)
        FRAME += 1

### META ###
def set_fps(fps):
    """sets the fps of the game"""
    global FPS
    FPS = fps
def get_fps():
    """returns the current fps of the game"""
    return round(gameclock.get_fps())
def set_name(name):
    """sets the name of the game"""
    global NAME
    NAME = name
    pygame.display.set_caption(NAME)
def get_frame():
    """returns the current frame of the game"""
    return FRAME


### DRAWING FUNCTIONS ###
def pset(x, y, color=7):
    """sets the pixel at the given coordinates to the given color"""
    SCREEN.set_at((x, y), COLORS[color])
def rect(x0, y0, x1, y1, color=7):
    """draws a rectangle"""
    pygame.draw.rect(SCREEN, COLORS[color], (x0, y0, x1-x0, y1-y0), 1)
def rectfill(x0, y0, x1, y1, color=7):
    """fills a rectangle"""
    pygame.draw.rect(SCREEN, COLORS[color], (x0, y0, x1-x0, y1-y0), 0)
def circ(x, y, r, color=7):
    """draws a circle"""
    pygame.draw.circle(SCREEN, COLORS[color], (x, y), r)
def circfill(x, y, r, color=7):
    """fills a circle"""
    pygame.draw.circle(SCREEN, COLORS[color], (x, y), r, 0)
def line(x0, y0, x1, y1, color=7):
    """draws a line"""
    pygame.draw.line(SCREEN, COLORS[color], (x0, y0), (x1, y1))
def oval(x0, y0, x1, y1, color=7):
    """draws an oval"""
    pygame.draw.ellipse(SCREEN, COLORS[color], (x0, y0, x1, y1), width=1)
def ovalfill(x0, y0, x1, y1, color=7):
    """fills an oval"""
    pygame.draw.ellipse(SCREEN, COLORS[color], (x0, y0, x1, y1), 0)
def gprint(text, x, y, color=7):
    """
    This function does not use the built-in text funciton, but replicates pico-8 character font and displays it pixel per pixel.
    Fonts are loaded from the font.py file.
    Text is converted to uppercase and accents are removed.
    """
    # split the text in characters
    text = str(text).upper()
    chars = [c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn']
    for c in range(len(chars)) :
        char = chars[c] 
        if char in FONT.keys():
            cMat = FONT[char]
        else : 
            cMat = FONT['?']
        
        # draw the character
        for i in range(len(cMat)) :
            for j in range(len(cMat[i])) :
                if cMat[i][j] == 1 :
                    pset(x+ c*4 + j, y + i, color)

def spr(x, y, spr):
    """
    draws a sprite.
    A sprite is a matrix of pixel colors.
    any color index that is not between 0 and 15 means transparent.
    """
    for i in range(len(spr)):
        for j in range(len(spr[0])):
            if spr[i][j] in range(16):
                pset(x+j, y+i, spr[i][j])


def pget(x, y):
    """returns the color of the pixel at the given coordinates"""
    pixel = SCREEN.get_at((x, y))
    pixelRGB = (pixel[0], pixel[1], pixel[2])
    index = COLORS.index(pixelRGB)
    return index
def cls(color=0):
    """clears the screen"""
    SCREEN.fill(COLORS[color])


### INPUT ###
def btn(button):
    """returns if the button is currently pressed or not"""
    return pygame.key.get_pressed()[INPUT[button.lower()]]
def btnp(button):
    """
    returns if the button was just pressed, aka only once
    to do this we use a dictionary that stores the state of the button at each frame before the update function.
    if the btn(button) returns true but the state is false in the dictionary, then the button was just pressed.
    """
    return KEYPRESSEVENTS[button.lower()] == 1
def btnr(button):
    """returns if the button was just released"""
    return KEYPRESSEVENTS[button.lower()] == 3

class Vector2():
    """
    A class that represents a 2D vector.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)
    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)
    def __str__(self):
        return "Vector2({}, {})".format(self.x, self.y)
    def __repr__(self):
        return "Vector2({}, {})".format(self.x, self.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))
    def __round__(self):
        return Vector2(round(self.x), round(self.y))
    def __floor__(self):
        return Vector2(math.floor(self.x), math.floor(self.y))
    def __ceil__(self):
        return Vector2(math.ceil(self.x), math.ceil(self.y))
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector2 only has 2 dimensions")
    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector2 only has 2 dimensions")
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    def normalize(self):
        """
        Normalizes the vector.
        Returns a new vector with the same direction but a length of 1.
        """
        length = self.length()
        if length == 0:
            return Vector2(0, 0)
        return Vector2(self.x / length, self.y / length)
    

# Printing welcome message (can be disabled in the options later)
if WELCOME:
    print("\n")
    info(f"Welcome to pyco-8 ! Version 0.1.0 (DEV) | Pygame version : {pygame.version.ver} | Python version : {platform.python_version()}\n")

if __name__ == "__main__":
    error("This file contains the source code of the engine. It is not meant to be run directly. Please run main.py instead.")