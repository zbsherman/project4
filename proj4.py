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
class puck(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'hockeyplayer.png'))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x -= 5



defen1 = defender()
defen2 = defender()
net = net()
allsprites = pygame.sprite.Group()
defs = pygame.sprite.Group()
pucks = pygame.sprite.Group()
nets = pygame.sprite.Group()
nets.add(net)
defs.add(defen1)
defs.add(defen2)

defsandgoal = RenderPlain(defen1,defen2,net)
pygame.display.update()

bg = pygame.image.load(os.path.join('images', 'halfrink.jpg'))
player = pygame.image.load(os.path.join('images', 'hockeyplayer.png'))
#puck = pygame.image.load(os.path.join('images', 'puck.png'))
#defender = pygame.image.load(os.path.join('images', 'defender.png'))

f = font.Font(None, 25)
goals = 0

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
        if event.key == pygame.K_SPACE:
            puck = puck()
            puck.rect.x = pos_x
            puck.rect.y = pos_y
            pucks.add(puck)
            allsprites.add(puck)
    for puck in pucks:
        goal = pygame.sprite.spritecollide(puck, nets, True)

        
        
        if event.key == pygame.K_LEFT:
            cheer.play()
            goals += 1
            defsandgoal.update()  



    if y_pos>= (HEIGHT-100):
        y_pos = HEIGHT-110
    elif y_pos <= 0:
        y_pos = 10

    

    gameDisplay.blit(bg, (bg_x, bg_y))
    gameDisplay.blit(player, (x_pos,y_pos))  
    t = f.render("Goals = " + str(goals), False, red)
    gameDisplay.blit(t, (320,0))
    defsandgoal.draw(gameDisplay)
    pygame.display.update()   






pygame.quit()
quit()
