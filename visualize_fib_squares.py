import pygame
from fibonacci_squares import make_rect, make_rects_random
from random import randint
from time import sleep

pygame.init()
window = (1600,1600)
screen = pygame.display.set_mode(window)

background = pygame.Surface(window)

background.fill ((255,90,0))

"""
for i in range(1, 40):
    rectangle = make_rect(i, window)
    pygame.draw.rect(background,(randint(0, 255),randint(0, 255),randint(0, 255)), rectangle)
    sleep(0.5)
    screen.blit(background, (0, 0))
    pygame.display.flip()

"""

i =1
while i <= 1000:
    x = randint(0, 1600)
    y = randint(0, 1600)
    for j in range(1, 17):
        rectangle = make_rects_random(j, window, x, y)
        pygame.draw.rect(background,(randint(0, 255),randint(0, 255),randint(0, 255)), rectangle)
        sleep(0.1)
        screen.blit(background, (0, 0))
        pygame.display.flip()
    i += 1
    sleep(0.001)
        


#screen.blit(background, (0, 0))
#pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()


#### maybe add reverse effect that picks a random spot in the sequence to reverse down to 1 again