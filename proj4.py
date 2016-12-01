import pygame
import random
import os
from pygame import *
from pygame.display import *
from pygame.sprite import *
from pygame.mixer import *
from pygame.time import *
from pygame.locals import *
from random import *


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

#Sound
skate = pygame.mixer.Sound("skate.wav")
cheer = pygame.mixer.Sound("cheer.wav")
aw = pygame.mixer.Sound("aw.wav")

#Create surface
gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Hockey Star")


def redraw():
    gameDisplay.fill(white)

class defender(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'defender.png'))
        self.rect = self.image.get_rect()
        randy = randint(0,500)
        randx = randint(150, 600)
        self.rect.center = (randx, randy)

    def update(self):
        randx = randint(150, 600)
        randy = randint(0,500)
        self.rect.center = (randx,randy)

class net(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'hockeysidenet.png'))
        self.rect = self.image.get_rect()
        nety = randint(50,450)
        netx = 60
        self.rect.center = (netx,nety)

    def update(self):
        nety = randint(50,450)
        netx = 60
        self.rect.center = (netx, nety)

class Puck(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'puck.png'))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x -= 7


#Sprites and Sprite Groups
net = net()
nets = pygame.sprite.Group()
nets.add(net)
defs = pygame.sprite.Group()
pucks = pygame.sprite.Group()
defsandgoal = pygame.sprite.Group()
defsandgoal.add(net)


pygame.display.update()

bg = pygame.image.load(os.path.join('images', 'halfrink.jpg'))
player = pygame.image.load(os.path.join('images', 'hockeyplayer.png'))


f = font.Font(None, 25)
goals = 0
lives = 3

gameExit = False
while not gameExit:
    score = 0
    redraw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True



    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            y_pos -= 10
        if event.key == pygame.K_DOWN:
            y_pos += 10
        skate.play()
        if event.key == pygame.K_SPACE and len(pucks) == 0:
            puck1 = Puck()
            puck1.rect.x = x_pos
            puck1.rect.y = y_pos+80
            pucks.add(puck1)

    pucks.update()

    for puck in pucks:
        if len(defs) > 0:
            if len(pygame.sprite.spritecollide(puck1, defs, False) )> 0:
                pucks.remove(puck1)
                aw.play()
                lives -= 1
                defsandgoal.update()

        if pygame.sprite.collide_rect(net, puck1) == True:
            pucks.remove(puck1)
            goals += 1
            cheer.play()
            defsandgoal.update()
        if puck.rect.x < net.rect.x:
            pucks.remove(puck1)


    if y_pos>= (HEIGHT-100):
        y_pos = HEIGHT-110
    elif y_pos <= 0:
        y_pos = 10


    if goals == 1 and len(defsandgoal) == 1:
        defen1 = defender()
        defsandgoal.add(defen1)
        defs.add(defen1)
    if goals == 3 and len(defsandgoal) == 2:
        defen2 = defender()
        defsandgoal.add(defen2)
        defs.add(defen2)
    if goals == 5 and len(defsandgoal) == 3:
        defen3 = defender()
        defsandgoal.add(defen3)
        defs.add(defen3)
    if goals == 7 and len(defsandgoal) == 4:
        defen4 = defender()
        defsandgoal.add(defen4)
        defs.add(defen4)
    if goals == 9 and len(defsandgoal) == 5:
        defen5 = defender()
        defsandgoal.add(defen5)
        defs.add(defen5)


    gameDisplay.blit(bg, (bg_x, bg_y))
    gameDisplay.blit(player, (x_pos,y_pos)) 
    defsandgoal.draw(gameDisplay)
    pucks.draw(gameDisplay)
    t = f.render("Goals = " + str(goals), False, red)
    gameDisplay.blit(t, (200,0))
    g = f.render("Lives = " + str(lives), False, red)
    gameDisplay.blit(g, (400,0))


    if lives <= 0:
        gameDisplay.fill(white)
        s = f.render("Final Score = " + str(goals), False, red)
        e = f.render("Game Over, click to exit", False, red)
        gameDisplay.blit(s,(300,200))
        gameDisplay.blit(e, (300,400))
        if event.type == pygame.MOUSEBUTTONDOWN:
            gameExit = True


    pygame.display.update()   


pygame.quit()
quit()
