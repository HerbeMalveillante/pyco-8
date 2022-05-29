from engine import *



class Player():
    def __init__(self):
        self.x = 1
        self.y = 1
        self.size = 8
    
    def draw(self):
        gprint("?", self.x, self.y)
    
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
    set_fps(30)

def _update():
    p.move()
    
def _draw():
    cls(1)
    p.draw()


run(_init, _update, _draw)