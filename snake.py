#Snake game developed by Jacob Simmerman
import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Snake Game")

x = 50
y = 50
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = false
pygame.quit()