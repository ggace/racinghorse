import pygame

from status import *
import resultCode

import gameControl

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

gameController = gameControl.gameController(gameDisplay, pygame)

pygame.display.set_caption('말달려라')

gameController.reset()

while not app_finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                app_finished = True
            if event.key == pygame.K_RETURN :
                game_start = True

    if(game_start):
        if(gameController.start() == resultCode.GAME_END):
            game_start = False
        
    

    gameController.update()
    clock.tick(60)

pygame.quit()
quit()