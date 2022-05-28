from engine import *

def _init():
    success("Printing from _init()")

def _update():
    success("Printing from _update()")

def _draw():
    success("Printing from _draw()")


run(_init, _update, _draw)
