# Use pip install pygame

import pygame
import sys
import random

class snake():
    def __init__(self):
        self.length = 1
        self.position = [((screen_width/2),(screen_height/2))]
        self.direction = random.choice([right,left,up,down])
        self.color = (255,255,255)
        self.score = 0

    def get_head_position(self):
        return self.position[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (( (cur[0]+(x*gridsize)) % screen_width), (cur[1]+(y*gridsize))%screen_height)
        if len(self.position) > 2 and new in self.position[2:]:
            self.reset()
        else:
            self.position.insert(0,new)
            if len(self.position) > self.length:
                self.position.pop()

    def reset(self):
        self.length = 1
        self.position = [((screen_width/2),(screen_height/2))]
        self.direction = random.choice([right,left,up,down])
        self.score = 0

    def draw(self, surface):
        for p in self.position:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

class food():
    
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random)

    def draw(self, surface):
        pass

def drawGrid(surface):
    for y in range (0, int(grid_height)):
        for x in range (0,int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize,y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr= pygame.Rect((x*gridsize,y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (84, 194, 205), rr)


# Global variables

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

up = (0,-1)
down = (0,1)
right = (1,0)
left = (-1,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height),0,32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    drawGrid(surface)

    snake = snake()
    food =  food()

    score = 0

    myfont = pygame.font.SysFont("monospace", 16)

    while(True):
        clock.tick(10)
        snake.handle_keys()


main()