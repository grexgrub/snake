import pygame
import os
import random 
import time
from mob.setting.setting import *

class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.apple = pygame.image.load(os.getcwd() + "/assets/apple.jpg").convert()

    def rand_location(self, snake_x, snake_y):
        x = 32 * random.randint(0, 19)
        y = 32 * random.randint(0, 19)
        self.spawn_check(snake_x, snake_y, x, y)

    def spawn_check(self, snake_x, snake_y, x, y):
        for i in range(len(wallx)):
            if wallx[i] == x and wally[i] == y:
                return self.rand_location(snake_x, snake_y)
            elif i == len(wallx) - 1: 
                for j in range(len(snake_x)):
                    if snake_x[j] == x and snake_y[j] == y:
                        return self.rand_location(snake_x, snake_y)
                    elif j == len(snake_x) - 1: 
                        self.x = x 
                        self.y = y
    

    def spawn(self):
        self.screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

