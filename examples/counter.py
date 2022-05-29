# demo for the btnp and btnr functions, that detects when a button has been just pressed and just released.

from engine import *


class counter:
    c = 0
    d = 0

def _init():
    set_name("counter")
    set_fps(60)
    

def _update():
    if btnp("primary"):
        counter.c += 1
    if btnr("primary"):
        counter.d += 1

def _draw():
    cls(1)
    gprint(counter.c, 1, 1)
    gprint(counter.d, 1, 10)


run(_init, _update, _draw)