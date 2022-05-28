from engine import *

def _init():
    set_name("Hello World")
    set_fps(30)

def _draw():
    cls(1)
    gprint("Hello World!", 1, 1)

run(_init, None, _draw)