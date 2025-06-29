import pygame
from pygame.locals import *
pygame.init()

# Set up the display
width, height = 480,560
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Window")

#loading images
board = pygame.image.load('assets/main_board.png')
board = pygame.transform.scale(board, (480, 480))

Cross = pygame.image.load('assets/Cross.jpg')
Cross = pygame.transform.scale(Cross, (120, 120))

Circle = pygame.image.load('assets/Circle.jpg')
Circle = pygame.transform.scale(Circle, (120, 120))

#the nine positions on the board
positions = [
    (10, 90), (180, 90), (350, 90),
    (10, 260), (180,260), (350, 260),
    (10, 430), (180, 430), (350, 430)
]

board_state = [0,0,0,0,0,0,0,0,0]  # 0 for empty, 1 for Cross, 2 for Circle

# Main loop
running = True
while running:
    mouse_data = pygame.event.Event(MOUSEBUTTONUP, pos=(0, 0), button=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event)
        elif event.type == MOUSEBUTTONUP:
            print(event)
            mouse_data = event
    window.fill((255, 255, 255))
    window.blit(board, (0, 80))


    # Draw the board state
    for i in range(len(board_state)):
        if board_state[i] == 1:
            window.blit(Cross, positions[i])
        elif board_state[i] == 2:
            window.blit(Circle, positions[i])

# and 70 < mouse_data.pos[1] < 220
    if mouse_data.pos[0] < 140:
        if 75 < mouse_data.pos[1] < 220:
            board_state[0] = 1
        elif 250 < mouse_data.pos[1] < 390:
            board_state[3] = 1
        elif 420 < mouse_data.pos[1] < 560:
            board_state[6] = 1
    elif 140 < mouse_data.pos[0] < 310:
        if 75 < mouse_data.pos[1] < 220:
            board_state[1] = 1
        elif 250 < mouse_data.pos[1] < 390:
            board_state[4] = 1
        elif 420 < mouse_data.pos[1] < 560:
            board_state[7] = 1
    elif 340 < mouse_data.pos[0] < 480:
        if 75 < mouse_data.pos[1] < 220:
            board_state[2] = 1
        elif 250 < mouse_data.pos[1] < 390:
            board_state[5] = 1
        elif 420 < mouse_data.pos[1] < 560:
            board_state[8] = 1




    pygame.display.update()








# Quit Pygame
pygame.quit()
exit()