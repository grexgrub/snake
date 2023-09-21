import pygame, os, time

class MainMenu():
    def __init__(self, HEIGHT, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, HEIGHT/2, HEIGHT)
        self.font = pygame.font.SysFont('arial', 30)
    
    def draw_menu_container(self):
        pygame.draw.rect(self.screen, (0,0,0), self.rect)
        self.draw_game_name(self.screen)
        self.draw_menu()
        pygame.display.update()

    def draw_game_name(self, screen):
        screen.blit(self.font.render('SNAKE', True, (0,0,0)), (420, 40))

    def draw_menu(self):
        start = self.font.render('S - To Start Game', True, (255,255,255))
        setting = self.font.render('O - To Option', True, (255,255,255))
        esc = self.font.render('ESC - To Leave', True, (255,255,255))
        self.screen.blit(setting, (60, 300))
        self.screen.blit(start, (40, 260))
        self.screen.blit(esc, (50, 340))
        



