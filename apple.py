import pygame
import random
from setting import W,H

class Apple():
    def __init__(self,screen):
        self.screen = screen
        self.color = (255,0,0)
        self.radius = 10
        self.respawn()


    def respawn(self):
        self.x = random.randint(0,W)
        self.y = random.randint(0,H)
        self.location =( self.x,self.y)

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.location , self.radius)  

    def __str__(self):
        return("Type=Apple Class")



if __name__=="__main__":
    a = Apple()
    print(a)