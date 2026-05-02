import pygame
import sys
from setting import W,H, BG


pygame.init()

screen = pygame.display.set_mode([W,H])

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    screen.fill(BG)
    pygame.display.update()
    
