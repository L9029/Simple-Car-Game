import cfg
import pygame
from pygame.locals import *
import random
import os

pygame.init()

running = True

screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT)) # Size of the screen
screen.fill((60, 220, 220)) # This set the background color
pygame.display.set_caption("Cars") # This set title
speed = 1.5
counter = 0

# Road
road_w = int(cfg.WIDTH/1.6)
roadmark_w = int(cfg.WIDTH/80)

# Position of the car on the road
right_lane = cfg.WIDTH / 2 + road_w / 4
left_lane = cfg.WIDTH / 2 - road_w / 4

# Car player image load
car = pygame.image.load(cfg.car) # search the image
car_loc = car.get_rect() # Car rect
car_loc.center = right_lane, cfg.HEIGHT * 0.8 # Car location

# Car enemy image load
car2 = pygame.image.load(cfg.other_car) # search the image
car2_loc = car2.get_rect() # Car2 rect
car2_loc.center = left_lane, cfg.HEIGHT * 0.2 # Car2 location

left = 0
right = 0

# Score and highest path (some issues with this part of the code)
score = 0
highest_score = 0 if not os.path.exists(cfg.HIGHEST_SCORE_RECORD_FILEPATH) else int(open(cfg.HIGHEST_SCORE_RECORD_FILEPATH).read())

pygame.font.init()
font = pygame.font.Font(cfg.FONT_PATH, 40)

while running:
    # dificulty of the game
    counter += 1
    
    if counter == 3000:
        speed += 0.25
        counter = 0
        print("LEVEL UP! " + str(speed))
        score = score + 1
        if score > highest_score:
            highest_score = score
    
    #Animate enemy vehicle
    car2_loc[1] += speed
    
    if car2_loc[1] > cfg.HEIGHT:
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    
    #End game logic
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break
    
    #Game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        #Moving
        if event.type == KEYDOWN:
            # Move the car to the left
            if event.key in [K_a, K_LEFT] and left == 0:
                car_loc = car_loc.move([-(road_w / 2), 0])
                left = 1
                right = 1
            # Move the car to the right    
            if event.key in [K_d, K_RIGHT] and right == 1:
                car_loc = car_loc.move([(road_w / 2), 0])
                right = 0
                left = 0
    
    # Draw Graphics
    pygame.draw.rect(screen, (50, 50, 50), (cfg.WIDTH/2 - road_w/2, 0, road_w, cfg.HEIGHT)) # Road rect
    pygame.draw.rect(screen, (255, 255, 255), (cfg.WIDTH/2 - roadmark_w/2, 0, roadmark_w, cfg.HEIGHT)) # Road middle mark rect
    # Road right and left mark rect
    pygame.draw.rect(screen, (220, 240, 240), (cfg.WIDTH/2 - road_w/2 + roadmark_w * 2, 0, roadmark_w, cfg.HEIGHT))
    pygame.draw.rect(screen, (220, 240, 240), (cfg.WIDTH/2 + road_w/2 - roadmark_w * 3, 0, roadmark_w, cfg.HEIGHT))

    
    screen.blit(car, car_loc) # Car Graphic
    screen.blit(car2, car2_loc) # Car2 Graphic
    
    #Draw the score in the screen
    score_text = 'Score: {}'.format(score)
    score_text = font.render(score_text, True, (255,255,255))
    score_rect = score_text.get_rect()
    score_rect.topleft = [5, 5]
    screen.blit(score_text, score_rect)
    
    #Draw the highest score in the screen
    highest_score_text = 'Highest: {}'.format(highest_score)
    highest_score_text = font.render(highest_score_text, True, (255,255,255))
    highest_score_rect = highest_score_text.get_rect()
    highest_score_rect.topright = [800, 6]
    screen.blit(highest_score_text, highest_score_rect)
    pygame.display.update()

# Saving the score
fp = open(cfg.HIGHEST_SCORE_RECORD_FILEPATH, 'w')
fp.write(str(highest_score))
fp.close()

pygame.quit()