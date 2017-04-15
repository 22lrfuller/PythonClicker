import pygame
import exampleSettings
import exampleSubfile
pygame.init()
exampleSettings.init()
exampleSubfile.globalVar()

one = exampleSettings.myList["one"]
two = exampleSettings.myList["two"]
three = exampleSettings.myList["three"]

done = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = (500, 500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Game")
font = pygame.font.SysFont('Calibri', 20, True, False)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(WHITE)

    screen.blit(font.render(str(printVar1), True, BLACK), [250, 150])
    screen.blit(font.render(str(printVar2), True, BLACK), [250, 250])
    screen.blit(font.render(str(printVar3), True, BLACK), [250, 350])

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()