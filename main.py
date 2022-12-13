import cfg
import pygame
from pygame.locals import *

pygame.init()

running = True

screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()