import pygame
from pygame.locals import *
pygame.init()

# Set up the display
width, height = 720,720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Window")

#loading images
board = pygame.image.load('assets/main board.jpg')
#board = board.get_rect()


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    


    window.fill((255, 255, 255))
    pygame.display.update()








# Quit Pygame
pygame.quit()
exit()