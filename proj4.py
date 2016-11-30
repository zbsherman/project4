import pygame
from pygame import *
from pygame.display import *
import random
import os

pygame.init();
WIDTH = 800
HEIGHT = 600

#Colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#Pos Var
x_pos = 0
y_pos = 550
bg_x = 0
bg_y = 0
poop_x = 0
poop_y = 0
newx = poop_x
newy = poop_y


#Create surface
gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Brickbreaker")


def redraw():
    gameDisplay.fill(black)

#class 
pygame.display.update()

#bg = pygame.image.load(os.path.join('images', 'whitehouse.bmp'))
pad = pygame.image.load(os.path.join('images', 'drake.png'))
poop = pygame.image.load(os.path.join('images', 'hockeynet.png'))
circ = pygame.draw.circle(gameDisplay, green,(newx, newy), 12)

gameExit = False
while not gameExit:
    redraw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_pos -= 10
        if event.key == pygame.K_RIGHT:
            x_pos += 10
       # if event.key == pygame.K_SPACE:
 #           newx = x_pos
 #           newy = y_pos
            #while newy < 600:
 #               circ
 #               newy += 50           
                 
 #   gameDisplay.blit(bg, (bg_x, bg_y))
    gameDisplay.blit(pad, (x_pos,y_pos))
    gameDisplay.blit(poop, (poop_x,poop_y))

    if x_pos>=(WIDTH-50):
        x_pos = 1
    elif x_pos <= 0:
        x_pos = WIDTH-1 
            
    pygame.display.update()     





pygame.quit()
quit()
