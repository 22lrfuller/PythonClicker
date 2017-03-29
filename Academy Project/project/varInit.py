import pygame
pygame.init()

def varDef():
	#Defining Some Variables
	global upgradeShow, done, menuShowVar, menuShow, pos, switch, clicks, cpcPrice, cpc, buyMultiVar, multiButtonNum, autoClickers1, autoClickers2, autoClickers3, autoClickers4, autoClickers5, autoClickers6, autoClickers7, autoClickers8, movingTextVar1, movingTextVar2, movingTextVar3, movingTextVar4, movingTextVar5, movingTextVar6, movingTextVar7, movingTextVar8, price1, price2, price3, price4, price5, price6, price7, price8, RAIN1, RAIN2, RAIN3, RAIN4, RAIN5, RAIN6, RAIN7, RAIN8, LIGHT_BLUE, LIGHT_PURPLE, BLACK, WHITE, GREEN, RED, BLUE, PURPLE, TEAL, ORANGE

	upgradeShow = False
	done = False
	menuShowVar = 0
	menuShow = False
	pos = 0
	switch = 0
	clicks = 0
	cpcPrice = 2
	cpc = 1
	buyMultiVar = 1
	multiButtonNum = 1
	autoClickers1 = 0
	autoClickers2 = 0
	autoClickers3 = 0
	autoClickers4 = 0
	autoClickers5 = 0
	autoClickers6 = 0
	autoClickers7 = 0
	autoClickers8 = 0
	movingTextVar1 = 0
	movingTextVar2 = 0
	movingTextVar3 = 0
	movingTextVar4 = 0
	movingTextVar5 = 0
	movingTextVar6 = 0
	movingTextVar7 = 0
	movingTextVar8 = 0
	price1 = 5
	price2 = 10
	price3 = 25
	price4 = 100
	price5 = 500
	price6 = 2500
	price7 = 5000
	price8 = 10000

	#Colors (Red, Green, Blue) - RAIN for Rainbow
	RAIN1 = (255, 255, 0)
	RAIN2 = (255, 225, 0)
	RAIN3 = (255, 195, 0)
	RAIN4 = (255, 165, 0)
	RAIN5 = (255, 135, 0)
	RAIN6 = (225, 135, 0)
	RAIN7 = (195, 105, 0)
	RAIN8 = (175, 95, 0)

	LIGHT_BLUE = (75, 200, 255)
	LIGHT_PURPLE = (255, 125, 255)
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	GREEN = (0, 255, 0)
	RED = (200, 0, 0)
	BLUE = (0, 0, 255)
	PURPLE = (255, 0, 255)
	TEAL = (75, 240, 190)
	ORANGE = (255, 175, 75)

	largeFont = pygame.font.SysFont('Calibri', 30, True, False)
	smallFont = pygame.font.SysFont('Calibri', 13, True, False)
	font = pygame.font.SysFont('Calibri', 20, True, False)
	size = (750, 750)
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	pygame.display.set_caption("Pygame Game")
	addingClick = pygame.draw.rect(screen, TEAL, (350, 300, 150, 200))