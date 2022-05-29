from engine import *
import math

# Top-Down

class Wall():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        rect(self.x, self.y, self.x + self.w, self.y + self.h)
        

walls = [Wall(100, 100, 10, 10)]

class Player():
    def __init__(self):

        self.x = 50
        self.y = 50
        self.velocity = Vector2(0, 0)
        self.width = 0
        self.height = 0
        self.speed = 1

        self.sprite = [[2 for i in range (5)] for j in range(5)]
    
    def update(self):
        if btn("up"):
            self.velocity.y = -1
        elif btn("down"):
            self.velocity.y = 1
        else:
            self.velocity.y = 0
        if btn("left"):
            self.velocity.x = -1
        elif btn("right"):
            self.velocity.x = 1
        else:
            self.velocity.x = 0
        
        self.velocity = self.velocity.normalize()
        # self.velocity.x = round(self.velocity.x, 2)
        # self.velocity.y = round(self.velocity.y, 2)


        self.x += self.velocity.x * self.speed
        self.y += self.velocity.y * self.speed

        # self.x = int(self.x)
        # self.y = int(self.y)
    
    def draw(self):
        spr(int(self.x), int(self.y), self.sprite)
        gprint(self.velocity, 1, 1)
        gprint(f"({self.x}, {self.y})", 1, 7)

p = Player()



def _init():
    set_fps(60)
    set_name("Top-Down")

def _update():
    p.update()

def _draw():
    cls(1)
    p.draw()
    for wall in walls:
        wall.draw()

run(_init, _update, _draw)