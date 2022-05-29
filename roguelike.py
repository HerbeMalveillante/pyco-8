from engine import *
import random


sprite = [
    [7,8,7],
    [8,9,8],
    [7,8,7]
]




class Player():
    def __init__(self):
        self.x = 1
        self.y = 1
        self.size = 3
    
    def draw(self):
        spr(self.x, self.y, sprite)
    
    def move(self):
        if btn("z"):
            self.y -= 1
        if btn("s"):
            self.y += 1
        if btn("q"):
            self.x -= 1
        if btn("d"):
            self.x += 1

p = Player()

def _init():
    set_name("RogueLike")
    set_fps(60)

def _update():
    p.move()
    
def _draw():
    cls(1)
    p.draw()
    for i in range(2000):
        # draw a random circle
        rect(random.randint(0, 128), random.randint(0, 128), random.randint(1, 30), random.randint(1, 30), random.randint(1, 15))
    rectfill(0, 0, 9, 7, 1)
    gprint(get_fps(), 1, 1)

run(_init, _update, _draw)