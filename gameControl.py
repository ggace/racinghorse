from colors import *
import time
import image

class gameController:
    gameDisplay: any
    pygame: any
    def __init__(self, gameDisplay, pygame):
        self.gameDisplay = gameDisplay
        self.pygame = pygame
        self.i = 1
        
        self.imageController = image.Image(self.gameDisplay, self.pygame)

    def start(self):
        self.imageController.draw_gif(f"resources/stop_horse/frame{i}.gif", [-40*9 + i*10 + 90*self.loop,0])
    
    def reset(self):
        self.gameDisplay.fill(WHITE) #하얀색으로 배경 채우기
        self.i = 1
        self.loop = 0
    
    def update(self):
        self.pygame.display.update()

    