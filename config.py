import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

### GRAPHICS ###
RESOLUTION = (128,128) # classic pico-8 resolution
ICON = "logo.png" # will be displayed in the taskbar and on the top left of the window
COLORS = [ # classic pico-8 colors
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


### INPUT ###

# INPUT = { # classic pico-8 input
#     "up": pygame.K_UP,
#     "down": pygame.K_DOWN,
#     "left": pygame.K_LEFT,
#     "right": pygame.K_RIGHT,
#     "action1": pygame.K_x,
#     "action2": pygame.K_c
# }

INPUT = { # extended keyset
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "primary": pygame.K_w,
    "secondary": pygame.K_x,
    "z": pygame.K_z,
    "q" : pygame.K_q,
    "s" : pygame.K_s,
    "d" : pygame.K_d,
    "e" : pygame.K_e,
    "a": pygame.K_a,
}