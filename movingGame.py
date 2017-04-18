import pygame
pygame.init()

x_speed = 0
y_speed = 0

x_coord = 250
y_coord = 250

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving Game")
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    done = True

    screen.fill(WHITE)

    if(event.type == pygame.KEYDOWN):
        if event.key == pygame.K_LEFT:
            x_speed = -3
        elif event.key == pygame.K_RIGHT:
            x_speed = 3
        elif event.key == pygame.K_UP:
            y_speed = -3
        elif event.key == pygame.K_DOWN:
            y_speed = 3

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_speed = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_speed = 0

    x_coord += x_speed
	y_coord += y_speed

	character = pygame.draw.rect(screen, BLACK, [x_coord, y_coord, 50, 50])

    pygame.display.flip()
    clock.tick(60) 
pygame.quit()