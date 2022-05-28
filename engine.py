import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import platform
from termcolor import cprint


# Features to implement :

# running function
# -> _init() | runs when the game starts
# -> _update() | runs every frame (30fps)
# -> _update60() | runs every frames (60fps)
# -> _draw() | runs every frame (30fps or 60fps depending on the update function that has been chosen)
# -> flip() | draw the graphics buffer to the screen (if not using the game loop)
# -> cls(color) | clear the graphics buffer

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
    pygame.init()
    pygame.display.set_mode((128, 128))

    info("Initializing game...")
    init()
    info("Game initialized.")
    info("Starting game loop...")
    while True:
        update()
        draw()
        pygame.display.flip()
        pygame.time.Clock().tick(30)




# Printing welcome message (can be disabled in the options later)
print("\n")
info(f"Welcome to pyco-8 ! Version 0.1.0 | Pygame version : {pygame.version.ver} | Python version : {platform.python_version()}\n")

if __name__ == "__main__":
    error("This file is not meant to be run directly. Please run main.py instead.")