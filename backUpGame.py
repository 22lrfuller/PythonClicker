from time import sleep
import pygame
pygame.init()

#Defining Some Variables
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

def movingText(autoClickNum):
    global autoUpgrade1
    global autoUpgrade2
    global autoUpgrade3
    global autoUpgrade4
    global autoUpgrade5
    global autoUpgrade6
    global autoUpgrade7
    global autoUpgrade8
    if(autoClickNum == 1):
        autoClickStr = len(str(autoClickers1))
        movingTextVar1 = 738 - (autoClickStr - 1) * 10
        return movingTextVar1

    if(autoClickNum == 2):
        autoClickStr = len(str(autoClickers2))
        movingTextVar2 = 738 - (autoClickStr - 1) * 10
        return movingTextVar2

    if(autoClickNum == 3):
        autoClickStr = len(str(autoClickers3))
        movingTextVar3 = 738 - (autoClickStr - 1) * 10
        return movingTextVar3

    if(autoClickNum == 4):
        autoClickStr = len(str(autoClickers4))
        movingTextVar4 = 738 - (autoClickStr - 1) * 10
        return movingTextVar4

    if(autoClickNum == 5):
        autoClickStr = len(str(autoClickers5))
        movingTextVar5 = 738 - (autoClickStr - 1) * 10
        return movingTextVar5

    if(autoClickNum == 6):
        autoClickStr = len(str(autoClickers6))
        movingTextVar6 = 738 - (autoClickStr - 1) * 10
        return movingTextVar6

    if(autoClickNum == 7):
        autoClickStr = len(str(autoClickers7))
        movingTextVar7 = 738 - (autoClickStr - 1) * 10
        return movingTextVar7

    if(autoClickNum == 8):
        autoClickStr = len(str(autoClickers8))
        movingTextVar8 = 738 - (autoClickStr - 1) * 10
        return movingTextVar8

def buttonPress():
    global upgradeShow
    global switch
    global clicks
    global autoClickers1
    global autoClickers2
    global autoClickers3
    global autoClickers4
    global autoClickers5
    global autoClickers6
    global autoClickers7
    global autoClickers8
    global price1
    global price2
    global price3
    global price4
    global price5
    global price6
    global price7
    global price8
    global addingClick
    global cpc
    global cpcPrice
    global backButton
    global buyMultiButton
    global multiButtonNum
    global buyMultiVar
    global menuShowVar
    global menuShow
    if(event.type == pygame.MOUSEBUTTONDOWN):
        pos = pygame.mouse.get_pos()
        if(switch == 0):
            #Clicking Red Button
            if(clickButton.collidepoint(pos) and upgradeShow == False):
                clicks += cpc
                switch = 1

            #Buying Autoclickers
            if(autoClick1.collidepoint(pos) and upgradeShow == False):
                autoClickers1 += int(buyingButton(price1, 1)) * buyMultiVar
                price1 = buttonPricing(price1, 1)

            if(autoClick2.collidepoint(pos) and upgradeShow == False):
                autoClickers2 += int(buyingButton(price2, 1)) * buyMultiVar
                price2 = buttonPricing(price2, 2)

            if(autoClick3.collidepoint(pos) and upgradeShow == False):
                autoClickers3 += int(buyingButton(price3, 1)) * buyMultiVar
                price3 = buttonPricing(price3, 3)

            if(autoClick4.collidepoint(pos) and upgradeShow == False):
                autoClickers4 += int(buyingButton(price4, 1)) * buyMultiVar
                price4 = buttonPricing(price4, 4)

            if(autoClick5.collidepoint(pos) and upgradeShow == False):
                autoClickers5 += int(buyingButton(price5, 1)) * buyMultiVar
                price5 = buttonPricing(price5, 5)

            if(autoClick6.collidepoint(pos) and upgradeShow == False):
                autoClickers6 += int(buyingButton(price6, 1)) * buyMultiVar
                price6 = buttonPricing(price6, 6)

            if(autoClick7.collidepoint(pos) and upgradeShow == False):
                autoClickers7 += int(buyingButton(price7, 1)) * buyMultiVar
                price7 = buttonPricing(price7, 7)

            if(autoClick8.collidepoint(pos) and upgradeShow == False):
                autoClickers8 += int(buyingButton(price8, 1)) * buyMultiVar
                price8 = buttonPricing(price8, 8)

            #Click Upgrade
            if(addingClick.collidepoint(pos) and upgradeShow == True):
                cpc += int(buyingButton(cpcPrice, 2))
                cpcPrice = buttonPricing(cpcPrice, "cpcUp")

            #Back Button
            if(backButton.collidepoint(pos)):
                upgradeShow = False

            #Slide Menu Button
            if(slideMenu.collidepoint(pos)):
                menuShow = True

                if(menuShowVar == 2):
                    menuShowVar = 0
                if(menuShowVar == 0):
                    menuShow = False
                if(menuShowVar == 1):
                    menuShow = True
                menuShowVar += 1
                switch = 1

            #Multiple Buy Button
            if(buyMultiButton.collidepoint(pos) and upgradeShow == False):
                multiButtonNum += 1
                if(multiButtonNum > 3):
                    multiButtonNum = 1
                if(multiButtonNum == 1):
                    buyMultiVar = 1
                if(multiButtonNum == 2):
                    buyMultiVar = 5
                if(multiButtonNum == 3):
                    buyMultiVar = 10
                switch = 1

    if(event.type == pygame.MOUSEBUTTONUP):
        switch = 0

def buttonPricing(price, autoClicker):
    global clicks
    global buyMultiVar
    price = price
    if(round(int(clicks)) >= round(price * 1.15 ** buyMultiVar)): #Make price equal to what it should be
        clicks -= price * 1.15 ** buyMultiVar
        return price * (1.15 ** buyMultiVar)
        if(autoClicker == "cpcUp"):
            return price * (1.5 ** buyMultiVar)
    else:
        return price

def buyingButton(price, buttonType):
    global clicks
    global cpcPrice
    global switch
    global buyMultiVar
    if(buttonType == 1 and int(clicks)) >= round(price * 1.15 ** buyMultiVar):
        switch = 1
        return 1
    if(buttonType == 2 and int(clicks)) >= (round(cpcPrice * 1.5 ** buyMultiVar)):
        switch = 1
        return 1
    else:
        screen.blit(font.render("Not Enought Money!", True, BLACK), [145, 190])
        if(event.type == pygame.MOUSEBUTTONUP):
            switch = 1
            screen.blit(font.render("Not Enought Money!", False, BLACK), [145, 190])
        return 0

while not done:
    #Quit Sense
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    backButton = pygame.draw.rect(screen, ORANGE, (0, 0, 100, 100))
    testButton = pygame.draw.rect(screen, TEAL, (100, 100, 300, 300))

    screen.fill(LIGHT_BLUE)
    buttonPress()

    if(menuShow == True):
        for x in range(0, 100):
            slideMenu = pygame.draw.rect(screen, LIGHT_PURPLE, ((0 + x), 25, 100, 50))
            sleep(0.005)
            slideMenu = pygame.draw.rect(screen, WHITE, ((0 + x), 25, 100, 50))
            sleep(0.005)

    #Defining Game Variable
    clickText = font.render("Clicks: " + str(round(clicks)), True, BLACK)
    clickUpgrade = font.render("Click Upgrades: " + str(round(cpc) - 1), True, BLACK)
    autoUpgrade1 = font.render(str(round(autoClickers1)), True, BLACK)
    autoUpgrade2 = font.render(str(round(autoClickers2)), True, BLACK)
    autoUpgrade3 = font.render(str(round(autoClickers3)), True, BLACK)
    autoUpgrade4 = font.render(str(round(autoClickers4)), True, BLACK)
    autoUpgrade5 = font.render(str(round(autoClickers5)), True, BLACK)
    autoUpgrade6 = font.render(str(round(autoClickers6)), True, BLACK)
    autoUpgrade7 = font.render(str(round(autoClickers7)), True, BLACK)
    autoUpgrade8 = font.render(str(round(autoClickers8)), True, BLACK)
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
    if(upgradeShow == False):
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
        slideMenu = pygame.draw.rect(screen, LIGHT_PURPLE, (0, 25, 100, 50))

        price1 = settings.pythonVariables['price1']
        price2 = settings.pythonVariables['price2']
        price3 = settings.pythonVariables['price3']
        price4 = settings.pythonVariables['price4']
        price5 = settings.pythonVariables['price5']
        price6 = settings.pythonVariables['price6']
        price7 = settings.pythonVariables['price7']
        price8 = settings.pythonVariables['price8']

        if(multiButtonNum == 1):
            buyOneText = font.render("Buy One", True, BLACK)
            screen.blit(buyOneText, [615, 670])

            buttonPrice1 = font.render(str(round(price1)), True, BLACK)
            buttonPrice2 = font.render(str(round(price2)), True, BLACK)
            buttonPrice3 = font.render(str(round(price3)), True, BLACK)
            buttonPrice4 = font.render(str(round(price4)), True, BLACK)
            buttonPrice5 = font.render(str(round(price5)), True, BLACK)
            buttonPrice6 = font.render(str(round(price6)), True, BLACK)
            buttonPrice7 = font.render(str(round(price7)), True, BLACK)
            buttonPrice8 = font.render(str(round(price8)), True, BLACK)

        if(multiButtonNum == 2):
            buyFiveText = font.render("Buy Five", True, BLACK)
            screen.blit(buyFiveText, [615, 670])

            buttonPrice1 = font.render(str(round(price1 * (1.15 ** 5))), True, BLACK)
            buttonPrice2 = font.render(str(round(price2 * (1.15 ** 5))), True, BLACK)
            buttonPrice3 = font.render(str(round(price3 * (1.15 ** 5))), True, BLACK)
            buttonPrice4 = font.render(str(round(price4 * (1.15 ** 5))), True, BLACK)
            buttonPrice5 = font.render(str(round(price5 * (1.15 ** 5))), True, BLACK)
            buttonPrice6 = font.render(str(round(price6 * (1.15 ** 5))), True, BLACK)
            buttonPrice7 = font.render(str(round(price7 * (1.15 ** 5))), True, BLACK)
            buttonPrice8 = font.render(str(round(price8 * (1.15 ** 5))), True, BLACK)

        if(multiButtonNum == 3):
            buyTenText = font.render("Buy Ten", True, BLACK)
            screen.blit(buyTenText, [615, 670])

            buttonPrice1 = font.render(str(round(price1 * (1.15 ** 10))), True, BLACK)
            buttonPrice2 = font.render(str(round(price2 * (1.15 ** 10))), True, BLACK)
            buttonPrice3 = font.render(str(round(price3 * (1.15 ** 10))), True, BLACK)
            buttonPrice4 = font.render(str(round(price4 * (1.15 ** 10))), True, BLACK)
            buttonPrice5 = font.render(str(round(price5 * (1.15 ** 10))), True, BLACK)
            buttonPrice6 = font.render(str(round(price6 * (1.15 ** 10))), True, BLACK)
            buttonPrice7 = font.render(str(round(price7 * (1.15 ** 10))), True, BLACK)
            buttonPrice8 = font.render(str(round(price8 * (1.15 ** 10))), True, BLACK)

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
        screen.blit(slideMenuText, [20, 40])
        screen.blit(autoUpgrade1, [movingText(1), 45])
        screen.blit(autoUpgrade2, [movingText(2), 120])
        screen.blit(autoUpgrade3, [movingText(3), 195])
        screen.blit(autoUpgrade4, [movingText(4), 270])
        screen.blit(autoUpgrade5, [movingText(5), 345])
        screen.blit(autoUpgrade6, [movingText(6), 420])
        screen.blit(autoUpgrade7, [movingText(7), 495])
        screen.blit(autoUpgrade8, [movingText(8), 570])

    #Updater
    clicks += (autoClickers1 * 2 + autoClickers2 * 5 + autoClickers3 * 7.5 + autoClickers4 * 15 + autoClickers5 * 25 + autoClickers6 * 50 + autoClickers7 * 75 + autoClickers8 * 100) / 100
    pygame.display.flip()
    clock.tick(100)

pygame.quit()