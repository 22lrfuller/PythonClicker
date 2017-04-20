import pygame
import settings
settings.init()
pygame.init()

screen = pygame.display.set_mode((750, 750))
TEAL = (75, 240, 190)

def pygameVar():
	#Defining Some Variables
	settings.pythonVariables['cpcButtonAmount'] = 0
	settings.pythonVariables['backButtonSwitch'] = 0
	settings.pythonVariables['menuButtonSwitch'] = 0
	settings.pythonVariables['buttonShowVar'] = 0
	settings.pythonVariables['clicks'] = 0
	settings.pythonVariables['switch'] = 0
	settings.pythonVariables['upgradeShow'] = False
	settings.pythonVariables['clicks'] = 0
	settings.pythonVariables['menuShow'] = False
	settings.pythonVariables['menuShowVar'] = 0
	settings.pythonVariables['done'] = False
	settings.pythonVariables['cpcPrice'] = 2
	settings.pythonVariables['cpc'] = 1
	settings.pythonVariables['buyMultiVar'] = 0
	settings.pythonVariables['multiButtonNum'] = 1
	settings.pythonVariables['autoClickers1'] = 0
	settings.pythonVariables['autoClickers2'] = 0
	settings.pythonVariables['autoClickers3'] = 0
	settings.pythonVariables['autoClickers4'] = 0
	settings.pythonVariables['autoClickers5'] = 0
	settings.pythonVariables['autoClickers6'] = 0
	settings.pythonVariables['autoClickers7'] = 0
	settings.pythonVariables['autoClickers8'] = 0
	settings.pythonVariables['movingTextVar1'] = 0
	settings.pythonVariables['movingTextVar2'] = 0
	settings.pythonVariables['movingTextVar3'] = 0
	settings.pythonVariables['movingTextVar4'] = 0
	settings.pythonVariables['movingTextVar5'] = 0
	settings.pythonVariables['movingTextVar6'] = 0
	settings.pythonVariables['movingTextVar7'] = 0
	settings.pythonVariables['movingTextVar8'] = 0
	settings.pythonVariables['price1'] = 5
	settings.pythonVariables['price2'] = 10
	settings.pythonVariables['price3'] = 25
	settings.pythonVariables['price4'] = 100
	settings.pythonVariables['price5'] = 500
	settings.pythonVariables['price6'] = 2500
	settings.pythonVariables['price7'] = 5000
	settings.pythonVariables['price8'] = 10000

	#Colors (Red, Green, Blue) - RAIN for Rainbow
	settings.pythonVariables['RAIN1'] = (255, 255, 0)
	settings.pythonVariables['RAIN2'] = (255, 225, 0)
	settings.pythonVariables['RAIN3'] = (255, 195, 0)
	settings.pythonVariables['RAIN4'] = (255, 165, 0)
	settings.pythonVariables['RAIN5'] = (255, 135, 0)
	settings.pythonVariables['RAIN6'] = (225, 135, 0)
	settings.pythonVariables['RAIN7'] = (195, 105, 0)
	settings.pythonVariables['RAIN8'] = (175, 95, 0)

	#Other Colors
	settings.pythonVariables['LIGHT_BLUE'] = (75, 200, 255)
	settings.pythonVariables['LIGHT_PURPLE'] = (255, 125, 255)
	settings.pythonVariables['BLACK'] = (0, 0, 0)
	settings.pythonVariables['WHITE'] = (255, 255, 255)
	settings.pythonVariables['GREEN'] = (0, 255, 0)
	settings.pythonVariables['RED'] = (200, 0, 0)
	settings.pythonVariables['BLUE'] = (0, 0, 255)
	settings.pythonVariables['PURPLE'] = (255, 0, 255)
	settings.pythonVariables['TEAL'] = (75, 240, 190)
	settings.pythonVariables['ORANGE'] = (255, 175, 75)

	#Pygame Variables
	settings.pythonVariables['font'] = pygame.font.SysFont('Calibri', 20, True, False)
	settings.pythonVariables['largeFont'] = pygame.font.SysFont('Calibri', 30, True, False)
	settings.pythonVariables['smallFont'] = pygame.font.SysFont('Calibri', 13, True, False)
	settings.pythonVariables['screen'] = screen
	settings.pythonVariables['clock'] = pygame.time.Clock()
	settings.pythonVariables['addingClick'] = pygame.draw.rect(screen, TEAL, (350, 300, 150, 200))