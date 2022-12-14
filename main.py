import cfg
import pygame
from pygame.locals import *

pygame.init()

running = True

screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT)) # Size of the screen
screen.fill((60, 220, 220)) # This set the background color
pygame.display.set_caption("Cars") # This set title

# Road
road_w = int(cfg.WIDTH/1.6)
roadmark_w = int(cfg.WIDTH/80)

# Draw Graphics
pygame.draw.rect(screen, (50, 50, 50), (cfg.WIDTH/2 - road_w/2, 0, road_w, cfg.HEIGHT))
pygame.draw.rect(screen, (255, 255, 255), (cfg.WIDTH/2 - roadmark_w/2, 0, roadmark_w, cfg.HEIGHT))
pygame.draw.rect(screen, (220, 240, 240), (cfg.WIDTH/2 - road_w/2 + roadmark_w * 2, 0, roadmark_w, cfg.HEIGHT))
pygame.draw.rect(screen, (220, 240, 240), (cfg.WIDTH/2 + road_w/2 - roadmark_w * 3, 0, roadmark_w, cfg.HEIGHT))

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()