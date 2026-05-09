import pygame
import sys
from setting import W,H, BG
from apple import Apple
from snake import Snake
import time

pygame.init()

screen = pygame.display.set_mode([W,H])
apple = Apple(screen)
snake = Snake(screen)

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    screen.fill(BG)
    apple.draw()
    snake.move()
    snake.draw()
    pygame.display.update()
    time.sleep(0.1)
    
