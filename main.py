from engine import *


class a:
    x = 0
    y = 0

def _init():
    success("Printing from _init()")
    set_fps(60)
    set_name("DEVELOPMENT")

def _update():
    if btn("U"):
        a.y -= 1
    if btn("D"):
        a.y += 1
    if btn("L"):
        a.x -= 1
    if btn("R"):
        a.x += 1

def _draw():
    cls()

    pset(a.x, a.y, 7)
    pset(a.x+1, a.y, 7)
    pset(a.x, a.y+1, 7)
    pset(a.x+1, a.y+1, 7)


run(_init, _update, _draw)
