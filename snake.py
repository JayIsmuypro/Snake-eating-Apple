import pygame 
from setting import W,H
class Snake():
    def __init__(self,screen):
        self.screen = screen 
        self.color = (0,200,0)
        self.w = 10
        self.h = 10
        self.x = W//2
        self.y = H//2

    def draw(self):
        self.location =(self.x,self.y,self.w,self.h)
        pygame.draw.rect(self.screen,self.color,self.location)

    def move(self):
        self.x = self.x + 1
        