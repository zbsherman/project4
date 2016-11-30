import pygame
from pygame import *
from pygame.display import *
from pygame.sprite import *
import random
import os
from pygame.mixer import *
from pygame.time import *
from pygame.locals import *


pygame.init();
pygame.mixer.init()
WIDTH = 800
HEIGHT = 600

#Colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#Pos Var
x_pos = 700
y_pos = 0
bg_x = 0
bg_y = 0
netx = 23
nety = 200
defx = 60
defy = 400

#Sound
skate = pygame.mixer.Sound("skate.wav")
cheer = pygame.mixer.Sound("cheer.wav")

#Create surface
gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Hockey Star")


def redraw():
    gameDisplay.fill(white)

class defender(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.image.load(os.path.join('images', 'defender.png'))
        screen = pyghame.display.get_surface()
        self.rect.topleft = 10,10
        self.


pygame.display.update()
#score = 0
bg = pygame.image.load(os.path.join('images', 'halfrink.jpg'))
player = pygame.image.load(os.path.join('images', 'hockeyplayer.png'))
net = pygame.image.load(os.path.join('images', 'hockeysidenet.png'))
defender = pygame.image.load(os.path.join('images', 'defender.png'))

time = 10
pygame.time.set_timer(USEREVENT+1, 1000)

gameExit = False
while not gameExit:
    score = 0
    redraw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == USEREVENT+1:
            time -= 1

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            y_pos -= 10
        if event.key == pygame.K_DOWN:
            y_pos += 10
        if event.key == pygame.K_SPACE:
            newx = x_pos
            newy = y_pos
        skate.play()
        if event.key == pygame.K_LEFT:
            cheer.play()


          
                 


    if y_pos>= (HEIGHT-100):
        y_pos = HEIGHT-110
    elif y_pos <= 0:
        y_pos = 10

    gameDisplay.blit(bg, (bg_x, bg_y))
    gameDisplay.blit(player, (x_pos,y_pos))
    gameDisplay.blit(net, (netx,nety)) 
    gameDisplay.blit(defender, (defx,defy))           
    pygame.display.update()   
    if time == 0:
        gameExit = True 





pygame.quit()
quit()
