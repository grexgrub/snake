import pygame, os
from mob.setting.setting import *

class MapRender():
    def __init__(self, screen):
        self.screen = screen
        pygame.init()
        self.map = 'map satu'
        self.block = pygame.image.load(os.getcwd() + "/assets/block.jpg")
        self.running = True

    def draw_map(self):
        if self.map == 'map satu':
            self.draw_map_satu()
        elif self.map == 'map dua':
            self.draw_map_dua()
        else:
            pass

    def draw_map_satu(self):
        for i in range(len(map_satu)):
            for j in range(len(map_satu[i])):
                if map_satu[i][j] == 'x':
                    self.screen.blit(self.block, (j*32, i*32))
                    pygame.display.flip()
                else:
                    pass

    def aray_add(self):
        for i in range(len(map_satu)):
            for j in range(len(map_satu[i])):
                if map_satu[i][j] == 'x':
                    wallx.append(j*32)
                    wally.append(i*32)
                else:
                    pass


