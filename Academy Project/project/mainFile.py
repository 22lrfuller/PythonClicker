import pygame
import varInit
import settings
import gameLoop

#Starts Pygame
pygame.init()

#Defines List
settings.init()

#Defines Variables
varInit.pygameVar()

#Starts Game Loop
gameLoop.mainLoop()

#Stop Program
pygame.quit()