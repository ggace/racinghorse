from colors import *
import time


class Image:
    i: int
    loop: int
    gameDisplay: any
    pygame: any
    
    def __init__(self, gameDisplay, pygame):
        self.gameDisplay = gameDisplay
        self.pygame = pygame
        self.i = 1
        self.loop = 0

    def draw_gif(self, imgName:str, position:list, loop:int, size=None):
        self.draw_frame(imgName, [-40*9 + self.i*10 + 90*self.loop,0], size)
        if(self.i < 9):
            self.i += 1
        elif(self.loop < loop):
            self.loop += 1
            self.i = 1
        
        return;
    
    def draw_frame(self, imgName:str, position:list, size=None):
        self.show_img(imgName, position)
        print(-40*9 + self.i*10 + 90*self.loop)
        self.update()
        time.sleep(0.1)
        self.gameDisplay.fill(WHITE) #하얀색으로 배경 채우기
        self.update()

    def draw_stop_horse(self):
        
        self.draw_stop_horse_frame(self.i)
        if(self.i < 9):
            self.i += 1
        elif(self.loop < 3):
            self.loop += 1
            self.i = 1
        
        return;
    
    def draw_stop_horse_frame(self, i):
        self.show_img(f"resources/stop_horse/frame{i}.gif", [-40*9 + i*10 + 90*self.loop,0])
        print(-40*9 + i*10 + 90*self.loop)
        self.update()
        time.sleep(0.1)
        self.gameDisplay.fill(WHITE) #하얀색으로 배경 채우기
        self.update()
    
    def draw_riding_horse(self):
        self.draw_riding_horse_frame(self.i)
        if(self.i < 6):
            self.i += 1
        else:
            self.i = 1
        return;
    
    def draw_riding_horse_frame(self, i):
        self.show_img(f"resources/riding_horse/frame{i}.gif", [0,0])
        self.update()
        time.sleep(0.1)
        self.gameDisplay.fill(WHITE) #하얀색으로 배경 채우기
        self.update()
        

    def show_img(self, imgName:str, position:list, size=None):
        img = self.pygame.image.load(imgName)
        if(size != None):
            img = self.pygame.transform.scale(img, (40, 102))

        self.gameDisplay.blit(img, position)
    
    def update(self):
        self.pygame.display.update()