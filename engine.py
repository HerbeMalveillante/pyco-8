import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import platform
from termcolor import cprint


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
    pygame.init()
    SCREEN = pygame.display.set_mode((128, 128), flags=pygame.SCALED|pygame.RESIZABLE)
    pygame.display.set_caption(NAME)

    info("Initializing game...")
    init()
    info("Game initialized.")
    info("Starting game loop...")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
    return pygame.time.Clock().get_fps()



def set_name(name):
    """sets the name of the game"""
    global NAME
    NAME = name
    pygame.display.set_caption(NAME)


### DRAWING FUNCTIONS ###
def pset(x, y, color):
    """sets the pixel at the given coordinates to the given color"""
    SCREEN.set_at((x, y), COLORS[color])
def pget(x, y):
    """returns the color of the pixel at the given coordinates"""
    pixel = SCREEN.get_at((x, y))
    pixelRGB = (pixel[0], pixel[1], pixel[2])
    index = COLORS.index(pixelRGB)
    return index
def cls():
    """clears the screen"""
    SCREEN.fill(COLORS[0])


### INPUT ###
def btn(button):
    """returns if the button is currently pressed or not"""
    return pygame.key.get_pressed()[INPUT[button]]
def btnp(button):
    """returns if the button was just pressed, aka only once"""
    return pygame.key.get_pressed()[INPUT[button]] and not btn(button)

# Printing welcome message (can be disabled in the options later)
print("\n")
info(f"Welcome to pyco-8 ! Version 0.1.0 | Pygame version : {pygame.version.ver} | Python version : {platform.python_version()}\n")

if __name__ == "__main__":
    error("This file contains the source code of the engine. It is not meant to be run directly. Please run main.py instead.")