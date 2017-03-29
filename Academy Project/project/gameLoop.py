while not done:
    #Quit Sense
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    backButton = pygame.draw.rect(screen, ORANGE, (0, 0, 100, 100))
    testButton = pygame.draw.rect(screen, TEAL, (100, 100, 300, 300))

    screen.fill(LIGHT_BLUE)
    buttonPress()

    print(menuShow)

    if(menuShow == True):
        print("part two")
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