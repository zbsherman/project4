import pygame
from pygame import *
from pygame.display import *

pygame.init();

#Colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

x_pos = 0
y_pos = 0


#Create surface
gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("Brickbreaker")


def redraw():
    gameDisplay.fill(white)
    gameDisplay.fill(blue, rect=[50,50, 20,20])
    pygame.draw.circle(gameDisplay, red, (50,100), 20, 0)
    pygame.draw.lines(gameDisplay, red, False, [(100,100), (150,200), (200,100)], 1)

pygame.display.update()

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
		if event.key == pygame.K_UP:
			y_pos -= 10
		if event.key == pygame.K_DOWN:
			y_pos += 10
	
	gameDisplay.fill(blue, rect=[x_pos,y_pos, 20,20])
	pygame.display.update()		



pygame.quit()
quit()
