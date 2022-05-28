from engine import *
import random


GRID = 4 # power of 2

class Snake():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 2 # direction : 0 = up, 1 = right, 2 = down, 3 = left
        self.body = []
        self.apple = Apple(self)
        self.size = 3
        self.best_score = 0
        self.state = 0 # 0 = dead, 1 = playing
    
    def draw(self):
        for i in range(len(self.body)):
            rect(self.body[i][0]*GRID, self.body[i][1]*GRID, GRID, GRID, 3)
        rectfill(self.x*GRID, self.y*GRID, GRID, GRID, 11)
        self.apple.draw()

class Apple():
    def __init__(self, snake):
        self.x, self.y = random.randint(0, 128/GRID - 1), random.randint(0, 128/GRID - 1)
        while [self.x, self.y] in snake.body or (self.x, self.y) == (snake.x, snake.y):
            self.x = random.randint(0, 128/GRID - 1)
            self.y = random.randint(0, 128/GRID - 1)
    def draw(self):
        rectfill(self.x*GRID, self.y*GRID, GRID, GRID, 8)

snake = Snake()

def _init():
    success("Printing from _init()")
    set_fps(15)
    set_name("PROTOTYPE")

def _update():
    if snake.state == 1:
        # inputs :
        if btn("U") and snake.direction != 2:
            snake.direction = 0
        if btn("R") and snake.direction != 3:
            snake.direction = 1
        if btn("D") and snake.direction != 0:
            snake.direction = 2
        if btn("L") and snake.direction != 1:
            snake.direction = 3

        # updating the body
        snake.body.insert(0, [snake.x, snake.y])
        if len(snake.body) > snake.size:
            snake.body.pop()
        
        # movement :
        if snake.direction == 0:
            snake.y -= 1
        if snake.direction == 1:
            snake.x += 1
        if snake.direction == 2:
            snake.y += 1
        if snake.direction == 3:
            snake.x -= 1
        
        # if the snake is out of bounds, make it pass trough the screen
        if snake.x > 128/GRID - 1:
            snake.x = 0
        if snake.x < 0:
            snake.x = 128/GRID - 1
        if snake.y > 128/GRID - 1:
            snake.y = 0
        if snake.y < 0:
            snake.y = 128/GRID - 1

        
        # collision with the apple
        if snake.x == snake.apple.x and snake.y == snake.apple.y:
            snake.size += 1
            if snake.size > snake.best_score:
                snake.best_score = snake.size
            snake.apple = Apple(snake)
        
        # collision with the body
        for i in range(len(snake.body)):
            if snake.x == snake.body[i][0] and snake.y == snake.body[i][1]:
                snake.size = 3
                snake.direction = 2
                snake.x = 0
                snake.y = 0
                snake.body = []
                snake.state = 0
                break
                
    else : 
        if btn("U") or btn("R") or btn("D") or btn("L"):
            snake.state = 1
    

def _draw():
    cls(1)
    snake.draw()
    gprint(f"Score:{snake.size}", 1, 1)
    gprint(f"Best score: {snake.best_score}", 1, 121)

    if snake.state == 0:
        gprint("Press any button to start", 15, 60)
    


run(_init, _update, _draw)
