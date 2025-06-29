import pygame
from pygame.locals import *
pygame.init()
import win_check

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
player_number = 1
win = False

# Main loop
running = True
while running:
    mouse_data = pygame.event.Event(MOUSEBUTTONUP, pos=(0, 0), button=1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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

    # Draw on the board
    x, y = mouse_data.pos
    col = -1
    row = -1
    if x < 140:
        col = 0
    elif x < 310:
        col = 1
    elif x < 480:
        col = 2
    if 75 < y < 220:
        row = 0
    elif 250 < y < 390:
        row = 1
    elif 420 < y < 560:
        row = 2

    if row != -1 and col != -1:
        index = row * 3 + col
        if board_state[index] == 0 and not win:
            board_state[index] = player_number
            print(f"player {player_number} placed at index {index}")
            if board_state.count(1) > board_state.count(2):
                player_number = 2
            elif board_state.count(2) > board_state.count(1):
                player_number = 1
            elif board_state.count(1) == board_state.count(2):
                player_number = 1
            
    
    

    # Check for win condition
    if not win:
        win = win_check.win_check(board_state, win)

    pygame.display.update()
# Quit Pygame
pygame.quit()
exit()