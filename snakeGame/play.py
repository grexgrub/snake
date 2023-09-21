import pygame
from pygame.locals import *
from mob.snake import Snake
from mob.apple import Apple
from mob.main_menu import MainMenu
from mob.setting.setting import SIZE
from mob.setting.setting import map_satu 
from mob.map import MapRender
import sys
import os
import time
import random

HEIGHT = 32*20
WIDTH = 32*20

class Game:
    def __init__(self):
        pygame.init()
        self.location = 'main menu'
        self.surface = pygame.display.set_mode((HEIGHT, WIDTH))
        self.surface.fill((255,255,255))
        self.apple = Apple(self.surface)
        self.map = 'map satu'
        self.draw_map = MapRender(self.surface)
        self.snake = Snake(self.surface,self.apple, self.draw_map)
        self.main_menu = MainMenu(HEIGHT, self.surface)
        self.running = True
        pygame.display.flip()

    def game_over(self):
        for i in range(len(self.snake.x)):
            if i > 2:
                if self.snake.x[0] == self.snake.x[i]:
                    if self.snake.y[0] == self.snake.y[i]:
                        self.starting = False
                        self.gameOver = True
                        self.running = False
                        self.display_over()
                elif i == len(self.snake.x):
                    for j in range(len(wallx)):
                        if self.snake.x[0] == wallx[j]:
                            if self.snake.y[0] == wally[j]:
                                self.starting = False
                                self.gameOver = True
                                self.running = False
                                self.display_over()

    def start(self):
        self.running = False
        while self.starting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.starting = False
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.starting= False
                    elif event.key == K_w:
                        if self.snake.direction != 'down':
                            self.snake.change_direction('up')
                        pass
                    elif event.key == K_s:
                        if self.snake.direction != 'up': 
                            self.snake.change_direction('down')
                        pass
                    elif event.key == K_a:
                        if self.snake.direction != 'right':
                            self.snake.change_direction('left')
                        pass
                    elif event.key == K_d:
                        if self.snake.direction != 'left':
                            self.snake.change_direction('right')
                        pass

            if self.snake.x[0] == self.apple.x and self.snake.y[0] == self.apple.y:
                self.snake.eat() 

            self.snake.move()
            self.game_over()

    def run(self): 
        while self.running:
            self.main_menu.draw_menu_container()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.starting = False
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                    if event.key == K_s:
                        self.draw_map.aray_add()
                        self.apple.rand_location(self.snake.x, self.snake.y)
                        self.starting = True
                        self.start()
                        self.snake.draw()
                        self.apple.spawn()
                        pygame.display.update()
                    else: 
                        pass

    def display_over(self):
        while self.gameOver:
            font = pygame.font.SysFont('arial',30)
            self.surface.blit(font.render('GAME OVER', True, (0,0,0)), (WIDTH/2.8, HEIGHT/2))
            pygame.display.update()
                        
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.gameOver = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.gameOver = False
                    if event.key == K_s:
                        self.gameOver = False
                        self.starting = True
                        self.start()




game = Game()
game.run()

