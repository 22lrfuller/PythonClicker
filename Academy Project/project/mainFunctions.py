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
                print("This works")
                print(menuShow)
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

def quitGame():
    pygame.quit()

def startGame():
    pygame.init()