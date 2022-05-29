# performance demo for drawing an increasing number of rectangles of random size and position to the screen.
# on my machine, I have achieved consistent 60 FPS for more than 5000 shapes, and 30 fps for 15000 shapes.

from engine import *
import random

def _init():
    set_name("Benchmark : increasing number of rectangles")
    set_fps(120)
    
def _draw():
    f = get_frame()
    for i in range(f):
        # draw a random circle
        rectfill(random.randint(0, 128), random.randint(0, 128), random.randint(1, 10), random.randint(1, 10), random.randint(1, 15))
    rectfill(0, 0, 9, 7, 1)
    gprint(get_fps(), 1, 1)
    rectfill(0, 7, len(str(f)) * 4 + 1, 7, 1)
    gprint(f, 1, 8)

run(_init, None, _draw)