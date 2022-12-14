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
pygame.draw.rect(screen, (50, 50, 50), (cfg.WIDTH/2 - road_w/2, 0, road_w, cfg.HEIGHT)) # Road rect
pygame.draw.rect(screen, (255, 255, 255), (cfg.WIDTH/2 - roadmark_w/2, 0, roadmark_w, cfg.HEIGHT)) # Road middle mark rect
# Road right and left mark rect
pygame.draw.rect(screen, (220, 240, 240), (cfg.WIDTH/2 - road_w/2 + roadmark_w * 2, 0, roadmark_w, cfg.HEIGHT))
pygame.draw.rect(screen, (220, 240, 240), (cfg.WIDTH/2 + road_w/2 - roadmark_w * 3, 0, roadmark_w, cfg.HEIGHT))

# Car player image load
car = pygame.image.load(cfg.car) # search the image
car_loc = car.get_rect() # Car rect
car_loc.center = cfg.WIDTH / 2 + road_w / 4, cfg.HEIGHT * 0.8 # Car location

# Car enemy image load
car2 = pygame.image.load(cfg.other_car) # search the image
car2_loc = car2.get_rect() # Car2 rect
car2_loc.center = cfg.WIDTH / 2 - road_w / 4, cfg.HEIGHT * 0.2 # Car2 location

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.blit(car, car_loc) # Car Graphic
    screen.blit(car2, car2_loc) # Car2 Graphic
    pygame.display.update()

pygame.quit()