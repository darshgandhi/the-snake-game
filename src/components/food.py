import pygame, random
from snake import Snake

FOOD_SIZE = 60
SQAURE_SIZE = 80
BUFFER_SIZE = (SQAURE_SIZE-FOOD_SIZE)//2

class Food:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def drawFood(self, layer, color):
        pygame.draw.rect(layer, color, (self.x+BUFFER_SIZE, self.y+BUFFER_SIZE, FOOD_SIZE, FOOD_SIZE))
    
    def respawn(self, snake):
        # Generate new coordinates for the food
        x = random.randrange(0, 800, 80)
        y = random.randrange(0, 800, 80)

        while snake.checkInBody(x, y): 
            x = random.randrange(0, 800, 80)
            y = random.randrange(0, 800, 80)

        self.x = x
        self.y = y    