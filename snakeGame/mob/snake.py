import pygame
import os
import random 
import time
from mob.setting.setting import SIZE


class Snake:
    def __init__(self, screen, apple, mapp):
        self.length = 2
        self.screen = screen
        self.map = mapp
        self.x = [SIZE]*self.length
        self.y = [SIZE]*self.length
        self.block = pygame.image.load(os.getcwd()+ "/assets/block.jpg").convert()
        self.direction = 'right'
        self.apple = apple

    def grow(self):
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])

    def draw(self):
        self.screen.fill((255,255,255))
        for i in range(self.length):
            self.screen.blit(self.block, (self.x[i],self.y[i]))
        self.apple.spawn() 
        pygame.display.flip()

    def move(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'right':
            self.move_right()
        elif self.direction == 'down':
            self.move_down()
        elif self.direction == 'up':
            self.move_up()
        else:
            self.move_left()
        self.score()
        time.sleep(0.1)

    def score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"SCORE: {self.length - 2}", True, (0, 0, 0))
        self.screen.blit(score, (32*15, 10))
        pygame.display.update()


    def move_up(self):
            self.y[0] -= SIZE 
            self.draw()

    def move_down(self):
        self.y[0] += SIZE
        self.draw()

    def move_right(self):
        self.x[0] += SIZE
        self.draw()

    def move_left(self):
            self.x[0] -= SIZE 
            self.draw()
    
    def change_direction(self, direction):
        self.direction = direction

    def eat(self):
        self.apple.rand_location(self.x, self.y)
        self.length += 1
        self.grow()
        self.score()


