import pygame
import settings
import varInit
settings.init()
varInit.pygameVar()
pygame.init()

#This File only Variables
lastPrice = 0

#Define Variables From Dictionary
switch = settings.pythonVariables['switch']
menuButtonSwitch = settings.pythonVariables['menuButtonSwitch']
backButtonSwitch = settings.pythonVariables['backButtonSwitch']
menuShow = settings.pythonVariables['menuShow']
menuShowVar = settings.pythonVariables['menuShowVar']
buttonShowVar = settings.pythonVariables['buttonShowVar']
done = settings.pythonVariables['done']
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

def priceLoop(price, autoClicker):
    if(autoClicker == "cpcUp"):
        if(round(int(settings.pythonVariables['clicks'])) >= round(price)):
            settings.pythonVariables['clicks'] -= round(price)
            return price * 1.5
    if(round(int(settings.pythonVariables['clicks'])) >= round(price)):
        settings.pythonVariables['clicks'] -= round(price)
        return price * 1.15

def backButtonFunc(event, backButton, menuShowArg):
    global done, backButtonSwitch, menuShowVar, menuShow, pos, buyMultiVar, multiButtonNum, done, settings
    if(event.type == pygame.MOUSEBUTTONDOWN):
        pos = pygame.mouse.get_pos()
        if(backButtonSwitch == 0):
            if(slideMenu.collidepoint(pos)):
                buttonShowVar += 1
                if(buttonShowVar == 2):
                    buttonShowVar = 0
                if(buttonShowVar == 0):
                    menuShow = False
                if(buttonShowVar == 1):
                    menuShow = True
                backButtonSwitch = 1
                return menuShow
    if(event.type == pygame.MOUSEBUTTONUP):
        backButtonSwitch = 0
    return menuShowArg

def menuButton(event, slideMenu, menuShowArg):
    global done, menuButtonSwitch, menuShowVar, menuShow, pos, buyMultiVar, multiButtonNum, done, settings
    if(event.type == pygame.MOUSEBUTTONDOWN):
        pos = pygame.mouse.get_pos()
        if(menuButtonSwitch == 0):
            if(slideMenu.collidepoint(pos)):
                menuShowVar += 1
                if(menuShowVar == 2):
                    menuShowVar = 0
                if(menuShowVar == 0):
                    menuShow = False
                if(menuShowVar == 1):
                    menuShow = True
                menuButtonSwitch = 1
                return menuShow
    if(event.type == pygame.MOUSEBUTTONUP):
        menuButtonSwitch = 0
    return menuShowArg

def movingText(autoClickNum):
    global movingTextVar1, movingTextVar2, movingTextVar3, movingTextVar4, movingTextVar5, movingTextVar6, movingTextVar7, movingTextVar8

    if(autoClickNum == 1):
        autoClickStr = len(str(settings.pythonVariables['autoClickers1']))
        movingTextVar1 = 738 - (autoClickStr - 1) * 10
        return movingTextVar1

    if(autoClickNum == 2):
        autoClickStr = len(str(settings.pythonVariables['autoClickers2']))
        movingTextVar2 = 738 - (autoClickStr - 1) * 10
        return movingTextVar2

    if(autoClickNum == 3):
        autoClickStr = len(str(settings.pythonVariables['autoClickers3']))
        movingTextVar3 = 738 - (autoClickStr - 1) * 10
        return movingTextVar3

    if(autoClickNum == 4):
        autoClickStr = len(str(settings.pythonVariables['autoClickers4']))
        movingTextVar4 = 738 - (autoClickStr - 1) * 10
        return movingTextVar4

    if(autoClickNum == 5):
        autoClickStr = len(str(settings.pythonVariables['autoClickers5']))
        movingTextVar5 = 738 - (autoClickStr - 1) * 10
        return movingTextVar5

    if(autoClickNum == 6):
        autoClickStr = len(str(settings.pythonVariables['autoClickers6']))
        movingTextVar6 = 738 - (autoClickStr - 1) * 10
        return movingTextVar6

    if(autoClickNum == 7):
        autoClickStr = len(str(settings.pythonVariables['autoClickers7']))
        movingTextVar7 = 738 - (autoClickStr - 1) * 10
        return movingTextVar7

    if(autoClickNum == 8):
        autoClickStr = len(str(settings.pythonVariables['autoClickers8']))
        movingTextVar8 = 738 - (autoClickStr - 1) * 10
        return movingTextVar8

def buttonPress(event, autoClick1, autoClick2, autoClick3, autoClick4, autoClick5, autoClick6, autoClick7, autoClick8, buyMultiButton, clickButton, backButton):
    global done, switch, menuShowVar, menuShow, pos, cpcPrice, cpc, buyMultiVar, multiButtonNum, RAIN1, RAIN2, RAIN3, RAIN4, RAIN5, RAIN6, RAIN7, RAIN8, LIGHT_BLUE, LIGHT_PURPLE, BLACK, WHITE, GREEN, RED, BLUE, PURPLE, TEAL, ORANGE, done, settings

    if(event.type == pygame.MOUSEBUTTONDOWN):
        pos = pygame.mouse.get_pos()
        if(switch == 0):
            #Clicking Red Button
            if(clickButton.collidepoint(pos) and menuShow == False):
                settings.pythonVariables['clicks'] += cpc
                switch = 1

            #Buying Autoclickers
            if(autoClick1.collidepoint(pos) and menuShow == False):
                settings.pythonVariables['autoClickers1'] += int(buyingButton(settings.pythonVariables['price1'], 1, event)) * buyMultiVar if buyMultiVar != 0 else int(buyingButton(settings.pythonVariables['price1'], 1, event))
                settings.pythonVariables['price1'] = buttonPricing(settings.pythonVariables['price1'], 1)

            if(autoClick2.collidepoint(pos) and menuShow == False):
                settings.pythonVariables['autoClickers2'] += int(buyingButton(settings.pythonVariables['price2'], 1, event)) * buyMultiVar if buyMultiVar != 0 else int(buyingButton(settings.pythonVariables['price2'], 1, event))
                settings.pythonVariables['price2'] = buttonPricing(settings.pythonVariables['price2'], 2)

            if(autoClick3.collidepoint(pos) and menuShow == False):
                settings.pythonVariables['autoClickers3'] += int(buyingButton(settings.pythonVariables['price3'], 1, event)) * buyMultiVar if buyMultiVar != 0 else int(buyingButton(settings.pythonVariables['price3'], 1, event))
                settings.pythonVariables['price3'] = buttonPricing(settings.pythonVariables['price3'], 3)

            if(autoClick4.collidepoint(pos) and menuShow == False):
                settings.pythonVariables['autoClickers4'] += int(buyingButton(settings.pythonVariables['price4'], 1, event)) * buyMultiVar if buyMultiVar != 0 else int(buyingButton(settings.pythonVariables['price4'], 1, event))
                settings.pythonVariables['price4'] = buttonPricing(settings.pythonVariables['price4'], 4)

            if(autoClick5.collidepoint(pos) and menuShow == False):
                settings.pythonVariables['autoClickers5'] += int(buyingButton(settings.pythonVariables['price5'], 1, event)) * buyMultiVar if buyMultiVar != 0 else int(buyingButton(settings.pythonVariables['price5'], 1, event))
                settings.pythonVariables['price5'] = buttonPricing(settings.pythonVariables['price5'], 5)

            if(autoClick6.collidepoint(pos) and menuShow == False):
                settings.pythonVariables['autoClickers6'] += int(buyingButton(settings.pythonVariables['price6'], 1, event)) * buyMultiVar if buyMultiVar != 0 else int(buyingButton(settings.pythonVariables['price6'], 1, event))
                settings.pythonVariables['price6'] = buttonPricing(settings.pythonVariables['price6'], 6)

            if(autoClick7.collidepoint(pos) and menuShow == False):
                settings.pythonVariables['autoClickers7'] += int(buyingButton(settings.pythonVariables['price7'], 1, event)) * buyMultiVar if buyMultiVar != 0 else int(buyingButton(settings.pythonVariables['price7'], 1, event))
                settings.pythonVariables['price7'] = buttonPricing(settings.pythonVariables['price7'], 7)

            if(autoClick8.collidepoint(pos) and menuShow == False):
                settings.pythonVariables['autoClickers8'] += int(buyingButton(settings.pythonVariables['price8'], 1, event)) * buyMultiVar if buyMultiVar != 0 else int(buyingButton(settings.pythonVariables['price8'], 1, event))
                settings.pythonVariables['price8'] = buttonPricing(settings.pythonVariables['price8'], 8)

            #Multiple Buy Button
            if(buyMultiButton.collidepoint(pos) and menuShow == False):
                multiButtonNum += 1
                if(multiButtonNum > 3):
                    multiButtonNum = 1
                if(multiButtonNum == 1):
                    buyMultiVar = 0
                if(multiButtonNum == 2):
                    buyMultiVar = 5
                if(multiButtonNum == 3):
                    buyMultiVar = 10
                switch = 1
                settings.pythonVariables['multiButtonNum'] = multiButtonNum

            if(backButton.collidepoint(pos)):
                menuShow = False
                settings.pythonVariables['menuShow'] = menuShow
                switch = 1

    if(event.type == pygame.MOUSEBUTTONUP):
        switch = 0

def buttonPricing(price, autoClicker):
    global done, menuShowVar, menuShow, pos, switch, cpcPrice, cpc, buyMultiVar, multiButtonNum, autoClickers1, autoClickers2, autoClickers3, autoClickers4, autoClickers5, autoClickers6, autoClickers7, autoClickers8, movingTextVar1, movingTextVar2, movingTextVar3, movingTextVar4, movingTextVar5, movingTextVar6, movingTextVar7, movingTextVar8, done

    if(buyMultiVar == 0):
        return priceLoop(price, autoClicker)
    else:
        for i in range(buyMultiVar):
            return priceLoop(price, autoClicker)
    return price

def buyingButton(price, buttonType, event):
    global done, menuShowVar, menuShow, pos, switch, cpcPrice, cpc, buyMultiVar, multiButtonNum, autoClickers1, autoClickers2, autoClickers3, autoClickers4, autoClickers5, autoClickers6, autoClickers7, autoClickers8, movingTextVar1, movingTextVar2, movingTextVar3, movingTextVar4, movingTextVar5, movingTextVar6, movingTextVar7, movingTextVar8, done, screen

    if(buttonType == 1 and int(settings.pythonVariables['clicks'])) >= price:
        switch = 1
        return 1
    if(buttonType == 2 and int(settings.pythonVariables['clicks'])) >= price:
        switch = 1
        return 1
    else:
        screen.blit(font.render("Not Enought Money!", True, BLACK), [145, 190])
        if(event.type == pygame.MOUSEBUTTONUP):
            switch = 1
            screen.blit(font.render("Not Enought Money!", False, BLACK), [145, 190])
        return 0

def quitGame():
    pygame.quit()

def startGame():
    pygame.init()