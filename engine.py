import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import platform
from termcolor import cprint
from font import FONT
import unicodedata


# Features to implement :

# running function
# -> _init() | runs when the game starts
# -> _update() | runs every frame
# -> _draw() | runs every frame
# -> set_fps(fps) | set the fps of the game

# pixels
# -> pget(x, y) | returns the color of the pixel at the given coordinates
# -> pset(x, y, color) | sets the pixel at the given coordinates to the given color

# shapes
# -> rect(x0, y0, x1, y1, color)
# -> rectfill(x0, y0, x1, y1, color)
# -> circ(x, y, r, color)
# -> circfill(x, y, r, color)
# -> line(x0, y0, x1, y1, color)
# -> gprint(text, x, y, color)
# -> oval(x0, y0, x1, y1, color)
# -> ovalfill(x0, y0, x1, y1, color)

# controls
# the game has a set of controls that can be used to control the game
# four directional buttons : up, down, left, right
# two action buttons : action1, action2
# buttons will be customizable
# pico-8 supports two players, but pyco-8 will only support one at the moment.
#
# -> btn(button) | returns if the button is currently pressed or not.
# -> btnp(button) | returns if the button was just pressed, aka only once

# time
# -> time() | returns the current time in fractional seconds since the start of the game
# -> frames() | returns the current number of frames since the start of the game

FPS = 30
NAME = "pyco-8 game"
SCREEN = None
gameclock = pygame.time.Clock()


KEYPRESSEVENTS = {
    "U":0,
    "D":0,
    "L":0,
    "R":0,
    "A":0,
    "B":0
}


COLORS = [
    (0, 0, 0),
    (29, 43, 83),
    (126, 37, 83),
    (0, 135, 81),
    (171, 82, 54),
    (95, 87, 79),
    (194, 195, 199),
    (255, 241, 232),
    (255, 0, 77),
    (255, 163, 0),
    (255, 236, 39),
    (0, 228, 54),
    (41, 173, 255),
    (131, 118, 156),
    (255, 119, 168),
    (255, 204, 170)
]

INPUT = {
    "U": pygame.K_UP,
    "D": pygame.K_DOWN,
    "L": pygame.K_LEFT,
    "R": pygame.K_RIGHT,
    "A": pygame.K_w,
    "B": pygame.K_x
}

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
    pygame.init()
    SCREEN = pygame.display.set_mode((128, 128), flags=pygame.SCALED|pygame.RESIZABLE)
    pygame.display.set_caption(NAME)
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # this works
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



        # for key in KEYPRESSEVENTS.keys():
        #     if KEYPRESSEVENTS[key] == 2 and btn(key):
        #         print(f"Key {key} pressed")
        #         KEYPRESSEVENTS[key] = 0
        #         # 0 -> The key just got pressed
        #     if KEYPRESSEVENTS[key] == 2 and not btn(key):
        #         print(f"Key {key} released")
        #         KEYPRESSEVENTS[key] = 1
        #         # 1 -> The key just got released
        #     else : 
        #         KEYPRESSEVENTS[key] = 2
        #         # 2 -> The key is either still pressed or still not pressed
        
        update()
        draw()
        pygame.display.flip()
        gameclock.tick(FPS)

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


### DRAWING FUNCTIONS ###
def pset(x, y, color=7):
    """sets the pixel at the given coordinates to the given color"""
    SCREEN.set_at((x, y), COLORS[color])
def rect(x0, y0, x1, y1, color=7):
    """draws a rectangle"""
    pygame.draw.rect(SCREEN, COLORS[color], (x0, y0, x1, y1))
def rectfill(x0, y0, x1, y1, color=7):
    """fills a rectangle"""
    pygame.draw.rect(SCREEN, COLORS[color], (x0, y0, x1, y1), 0)
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
    pygame.draw.ellipse(SCREEN, COLORS[color], (x0, y0, x1, y1))
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
        for i in range(5) :
            for j in range(3) :
                if cMat[i][j] == 1 :
                    pset(x+ c*4 + j, y + i, color)


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
    return pygame.key.get_pressed()[INPUT[button]]
def btnp(button):
    """
    returns if the button was just pressed, aka only once
    to do this we use a dictionary that stores the state of the button at each frame before the update function.
    if the btn(button) returns true but the state is false in the dictionary, then the button was just pressed.
    """
    return KEYPRESSEVENTS[button] == 1
def btnr(button):
    """returns if the button was just released"""
    return KEYPRESSEVENTS[button] == 3
    

# Printing welcome message (can be disabled in the options later)
print("\n")
info(f"Welcome to pyco-8 ! Version 0.1.0 | Pygame version : {pygame.version.ver} | Python version : {platform.python_version()}\n")

if __name__ == "__main__":
    error("This file contains the source code of the engine. It is not meant to be run directly. Please run main.py instead.")