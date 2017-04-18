import pygame
from time import sleep
from mainFunctions import *
import settings
import varInit
settings.init()
varInit.pygameVar()
pygame.init()

#Define Variables
menuShow = settings.pythonVariables['menuShow']
switch = settings.pythonVariables['switch']
cpcPrice = settings.pythonVariables['cpcPrice']
cpc = settings.pythonVariables['cpc']
buyMultiVar = settings.pythonVariables['buyMultiVar']
multiButtonNum = settings.pythonVariables['multiButtonNum']
autoClickers1 = settings.pythonVariables['autoClickers1']
autoClickers2 = settings.pythonVariables['autoClickers2']
autoClickers3 = settings.pythonVariables['autoClickers3']
autoClickers4 = settings.pythonVariables['autoClickers4']
autoClickers5 = settings.pythonVariables['autoClickers5']
autoClickers6 = settings.pythonVariables['autoClickers6']
autoClickers7 = settings.pythonVariables['autoClickers7']
autoClickers8 = settings.pythonVariables['autoClickers8']
movingTextVar1 = settings.pythonVariables['movingTextVar1']
movingTextVar2 = settings.pythonVariables['movingTextVar2']
movingTextVar3 = settings.pythonVariables['movingTextVar3']
movingTextVar4 = settings.pythonVariables['movingTextVar4']
movingTextVar5 = settings.pythonVariables['movingTextVar5']
movingTextVar6 = settings.pythonVariables['movingTextVar6']
movingTextVar7 = settings.pythonVariables['movingTextVar7']
movingTextVar8 = settings.pythonVariables['movingTextVar8']
price1 = settings.pythonVariables['price1']
price2 = settings.pythonVariables['price2']
price3 = settings.pythonVariables['price3']
price4 = settings.pythonVariables['price4']
price5 = settings.pythonVariables['price5']
price6 = settings.pythonVariables['price6']
price7 = settings.pythonVariables['price7']
price8 = settings.pythonVariables['price8']

#Colors (Red, Green, Blue) - RAIN for Rainbow
RAIN1 = settings.pythonVariables['RAIN1']
RAIN2 = settings.pythonVariables['RAIN2']
RAIN3 = settings.pythonVariables['RAIN3']
RAIN4 = settings.pythonVariables['RAIN4']
RAIN5 = settings.pythonVariables['RAIN5']
RAIN6 = settings.pythonVariables['RAIN6']
RAIN7 = settings.pythonVariables['RAIN7']
RAIN8 = settings.pythonVariables['RAIN8']

#Other Colors
LIGHT_BLUE = settings.pythonVariables['LIGHT_BLUE']
LIGHT_PURPLE = settings.pythonVariables['LIGHT_PURPLE']
BLACK = settings.pythonVariables['BLACK']
WHITE = settings.pythonVariables['WHITE']
GREEN = settings.pythonVariables['GREEN']
RED = settings.pythonVariables['RED']
BLUE = settings.pythonVariables['BLUE']
PURPLE = settings.pythonVariables['PURPLE']
TEAL = settings.pythonVariables['TEAL']
ORANGE = settings.pythonVariables['ORANGE']

#Pygame Variables
font = settings.pythonVariables['font']
largeFont = settings.pythonVariables['largeFont']
smallFont = settings.pythonVariables['smallFont']
screen = settings.pythonVariables['screen']
clock = settings.pythonVariables['clock']
addingClick = settings.pythonVariables['addingClick']

def mainLoop():
    global menuShow, done, menuShowVar, menuShow, pos, switch, clicks, cpcPrice, cpc, buyMultiVar, multiButtonNum, movingTextVar1, movingTextVar2, movingTextVar3, movingTextVar4, movingTextVar5, movingTextVar6, movingTextVar7, movingTextVar8, price1, price2, price3, price4, price5, price6, price7, price8, RAIN1, RAIN2, RAIN3, RAIN4, RAIN5, RAIN6, RAIN7, RAIN8, LIGHT_BLUE, LIGHT_PURPLE, BLACK, WHITE, GREEN, RED, BLUE, PURPLE, TEAL, ORANGE, done, pythonVariables

    pygame.display.set_caption("Pygame Game")
    while not done:
        #Quit Sense
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        backButton = pygame.draw.rect(screen, ORANGE, (0, 0, 100, 100))
        testButton = pygame.draw.rect(screen, TEAL, (100, 100, 300, 300))

        screen.fill(LIGHT_BLUE)

        #Defining Game Variable
        clickText = font.render("Clicks: " + str(round(settings.pythonVariables['clicks'])), True, BLACK)
        clickUpgrade = font.render("Click Upgrades: " + str(round(settings.pythonVariables['cpc']) - 1), True, BLACK)
        autoUpgrade1 = font.render(str(round(settings.pythonVariables['autoClickers1'])), True, BLACK)
        autoUpgrade2 = font.render(str(round(settings.pythonVariables['autoClickers2'])), True, BLACK)
        autoUpgrade3 = font.render(str(round(settings.pythonVariables['autoClickers3'])), True, BLACK)
        autoUpgrade4 = font.render(str(round(settings.pythonVariables['autoClickers4'])), True, BLACK)
        autoUpgrade5 = font.render(str(round(settings.pythonVariables['autoClickers5'])), True, BLACK)
        autoUpgrade6 = font.render(str(round(settings.pythonVariables['autoClickers6'])), True, BLACK)
        autoUpgrade7 = font.render(str(round(settings.pythonVariables['autoClickers7'])), True, BLACK)
        autoUpgrade8 = font.render(str(round(settings.pythonVariables['autoClickers8'])), True, BLACK)
        clickMe = font.render("Click Me!", True, BLACK)
        buttonName1 = smallFont.render("First", True, BLACK)
        buttonName2 = smallFont.render("Second", True, BLACK)
        buttonName3 = smallFont.render("Third", True, BLACK)
        buttonName4 = smallFont.render("Fourth", True, BLACK)
        buttonName5 = smallFont.render("Fifth", True, BLACK)
        buttonName6 = smallFont.render("Sixth", True, BLACK)
        buttonName7 = smallFont.render("Seventh", True, BLACK)
        buttonName8 = smallFont.render("Eighth", True, BLACK)
        buttonAddingClick = font.render("Clicks per", True, BLACK)
        buttonAddingClick2 = font.render("Click", True, BLACK)
        backButtonName = font.render("Back", True, BLACK)
        priceForCpc = font.render(str(round(cpcPrice)), True, BLACK)
        buyOneText = font.render("Buy One", True, BLACK)
        buyFiveText = font.render("Buy Five", True, BLACK)
        buyTenText = font.render("Buy Ten", True, BLACK)
        slideMenuText = font.render("Menu", True, BLACK)

        #Game Buttons
        if(menuShow == False):
            autoClick1 = pygame.draw.rect(screen, RAIN1, (550, 0, 200, 75))
            autoClick2 = pygame.draw.rect(screen, RAIN2, (550, 75, 200, 75))
            autoClick3 = pygame.draw.rect(screen, RAIN3, (550, 150, 200, 75))
            autoClick4 = pygame.draw.rect(screen, RAIN4, (550, 225, 200, 75))
            autoClick5 = pygame.draw.rect(screen, RAIN5, (550, 300, 200, 75))
            autoClick6 = pygame.draw.rect(screen, RAIN6, (550, 375, 200, 75))
            autoClick7 = pygame.draw.rect(screen, RAIN7, (550, 450, 200, 75))
            autoClick8 = pygame.draw.rect(screen, RAIN8, (550, 525, 200, 75))
            buyMultiButton = pygame.draw.rect(screen, TEAL, (550, 600, 200, 200))
            clickButton = pygame.draw.rect(screen, RED, (140, 210, 200, 200))
            slideMenu = pygame.draw.rect(screen, LIGHT_PURPLE, (0, 0, 100, 50))

            if(multiButtonNum == 1):
                buyOneText = font.render("Buy One", True, BLACK)
                screen.blit(buyOneText, [615, 670])

                buttonPrice1 = font.render(str(round(settings.pythonVariables['price1'])), True, BLACK)
                buttonPrice2 = font.render(str(round(settings.pythonVariables['price2'])), True, BLACK)
                buttonPrice3 = font.render(str(round(settings.pythonVariables['price3'])), True, BLACK)
                buttonPrice4 = font.render(str(round(settings.pythonVariables['price4'])), True, BLACK)
                buttonPrice5 = font.render(str(round(settings.pythonVariables['price5'])), True, BLACK)
                buttonPrice6 = font.render(str(round(settings.pythonVariables['price6'])), True, BLACK)
                buttonPrice7 = font.render(str(round(settings.pythonVariables['price7'])), True, BLACK)
                buttonPrice8 = font.render(str(round(settings.pythonVariables['price8'])), True, BLACK)

            if(multiButtonNum == 2):
                buyFiveText = font.render("Buy Five", True, BLACK)
                screen.blit(buyFiveText, [615, 670])

                buttonPrice1 = font.render(str(round(settings.pythonVariables['price1'] * (1.15 ** 5))), True, BLACK)
                buttonPrice2 = font.render(str(round(settings.pythonVariables['price2'] * (1.15 ** 5))), True, BLACK)
                buttonPrice3 = font.render(str(round(settings.pythonVariables['price3'] * (1.15 ** 5))), True, BLACK)
                buttonPrice4 = font.render(str(round(settings.pythonVariables['price4'] * (1.15 ** 5))), True, BLACK)
                buttonPrice5 = font.render(str(round(settings.pythonVariables['price5'] * (1.15 ** 5))), True, BLACK)
                buttonPrice6 = font.render(str(round(settings.pythonVariables['price6'] * (1.15 ** 5))), True, BLACK)
                buttonPrice7 = font.render(str(round(settings.pythonVariables['price7'] * (1.15 ** 5))), True, BLACK)
                buttonPrice8 = font.render(str(round(settings.pythonVariables['price8'] * (1.15 ** 5))), True, BLACK)

            if(multiButtonNum == 3):
                buyTenText = font.render("Buy Ten", True, BLACK)
                screen.blit(buyTenText, [615, 670])

                buttonPrice1 = font.render(str(round(settings.pythonVariables['price1'] * (1.15 ** 10))), True, BLACK)
                buttonPrice2 = font.render(str(round(settings.pythonVariables['price2'] * (1.15 ** 10))), True, BLACK)
                buttonPrice3 = font.render(str(round(settings.pythonVariables['price3'] * (1.15 ** 10))), True, BLACK)
                buttonPrice4 = font.render(str(round(settings.pythonVariables['price4'] * (1.15 ** 10))), True, BLACK)
                buttonPrice5 = font.render(str(round(settings.pythonVariables['price5'] * (1.15 ** 10))), True, BLACK)
                buttonPrice6 = font.render(str(round(settings.pythonVariables['price6'] * (1.15 ** 10))), True, BLACK)
                buttonPrice7 = font.render(str(round(settings.pythonVariables['price7'] * (1.15 ** 10))), True, BLACK)
                buttonPrice8 = font.render(str(round(settings.pythonVariables['price8'] * (1.15 ** 10))), True, BLACK)

            screen.blit(buttonPrice1, [553, 22])
            screen.blit(buttonPrice2, [553, 97])
            screen.blit(buttonPrice3, [553, 172])
            screen.blit(buttonPrice4, [553, 247])
            screen.blit(buttonPrice5, [553, 322])
            screen.blit(buttonPrice6, [553, 397])
            screen.blit(buttonPrice7, [553, 472])
            screen.blit(buttonPrice8, [553, 547])

            #Autoclicker
            screen.blit(buttonName1, [553, 5])
            screen.blit(buttonName2, [553, 80])
            screen.blit(buttonName3, [553, 155])
            screen.blit(buttonName4, [553, 230])
            screen.blit(buttonName5, [553, 305])
            screen.blit(buttonName6, [553, 380])
            screen.blit(buttonName7, [553, 455])
            screen.blit(buttonName8, [553, 530])

            #Other Button Names
            screen.blit(clickMe, [200, 300])
            screen.blit(clickText, [0, 710])
            screen.blit(clickUpgrade, [0, 730])
            screen.blit(slideMenuText, [20, 20])
            screen.blit(autoUpgrade1, [movingText(1), 45])
            screen.blit(autoUpgrade2, [movingText(2), 120])
            screen.blit(autoUpgrade3, [movingText(3), 195])
            screen.blit(autoUpgrade4, [movingText(4), 270])
            screen.blit(autoUpgrade5, [movingText(5), 345])
            screen.blit(autoUpgrade6, [movingText(6), 420])
            screen.blit(autoUpgrade7, [movingText(7), 495])
            screen.blit(autoUpgrade8, [movingText(8), 570])

        if(menuShow == True):
            backButton = pygame.draw.rect(screen, RED, (0, 100, 100, 50))

        buttonPress(event, autoClick1, autoClick2, autoClick3, autoClick4, autoClick5, autoClick6, autoClick7, autoClick8, buyMultiButton, clickButton, backButton)
        menuShow = menuButton(event, slideMenu, menuShow)
        menuShow = menuButton(event, backButton, menuShow)

        #Updater
        settings.pythonVariables['clicks'] += (settings.pythonVariables['autoClickers1'] * 2 + settings.pythonVariables['autoClickers2'] * 5 + settings.pythonVariables['autoClickers3'] * 7.5 + settings.pythonVariables['autoClickers4'] * 15 + settings.pythonVariables['autoClickers5'] * 25 + settings.pythonVariables['autoClickers6'] * 50 + settings.pythonVariables['autoClickers7'] * 75 + settings.pythonVariables['autoClickers8'] * 100) / 100
        pygame.display.flip()
        clock.tick(100)