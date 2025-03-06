import pygame

def drawBoard(Window, HEIGHT, WIDTH): 
    pygame.draw.rect(Window, pygame.Color(95, 111, 86), (0, 0, WIDTH, HEIGHT))
    start = 0
    for y in range(0, HEIGHT, 80):
        for x in range(int(start), int(HEIGHT), 160):
            pygame.draw.rect(Window, pygame.Color(169, 179, 136), (x, y, 80, 80))
            if start == 0:
                start = WIDTH/10
            else:
                start = 0