import pygame, random
from src.components.snake import Snake
from food import Food
from src.utils.create_board import drawBoard

# WINDOW CONSTANTS
FPS = 60
WIDTH = int(800)
HEIGHT = int(800)

# SNAKE CONSTANTS
SCORE = -1
CENTRE = WIDTH//2
SNAKE_WIDTH = 80
SNAKE_COLOR = pygame.Color(255, 255, 255)

FOOD_COLOR = pygame.Color(255, 0, 0)
SQAURE_SIZE = 80


FOOD = {'x':None, 'y':None, 'exists':False}

def main():
    global SCORE, SNAKE_COLOR  # Add these global declarations at the beginning of the function
    run = True

    # CLOCK SET-UP
    clock = pygame.time.Clock()
    last_update_time = pygame.time.get_ticks() / 1000

    # WINDOW SET-UP
    Window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    SPRITE_IMAGE = pygame.image.load('assets\snake-graphics.png').convert_alpha()
    SPRITE_IMAGE.set_colorkey((0, 0, 0))

    background = pygame.Surface((WIDTH, HEIGHT))
    SNAKE_LAYER = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    FOOD_LAYER = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    game_state = "home screen"
    direction = 'right'
    snake = Snake(CENTRE, CENTRE, 'right', 'right')

    while run:

        # CLOCK SET-UP
        clock.tick(FPS)
        now = pygame.time.get_ticks() / 1000
        elapsed_time = now - last_update_time
        if now == 0:
            snake.increase_size()

        
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_UP and snake.direction != 'down':
                    direction = 'up'
                elif event.key == pygame.K_DOWN and snake.direction != 'up':
                    direction = 'down'
                elif event.key == pygame.K_LEFT and snake.direction != 'right': 
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and snake.direction != 'left':
                    direction = 'right'
                elif event.key == pygame.K_SPACE:
                        # Clear Screen
                        del image_surface 

                        # Update Gamestate
                        game_state = "running"
                        SCORE = -1
                        # Reset Snake & Food
                        snake = Snake(CENTRE, CENTRE, 'right', 'right')
                        x = random.randrange(0,800,80)
                        y = random.randrange(0,800,80)
                        while snake.x == x and snake.y == y:
                            x = random.randrange(0,800,80)
                            y = random.randrange(0,800,80)
                        food = Food(x, y)
                        food.drawFood(FOOD_LAYER, FOOD_COLOR)
                        # Draw Board
                        drawBoard(background, HEIGHT, WIDTH)
                        FOOD['exists'] = False
        
        if game_state == "running":
            # Clear the snake layer
            if SCORE < 1:
                SCORE += 1
                snake.increase_size()
            
            # Update snake position based on direction
            if elapsed_time >= 0.15:
                SNAKE_LAYER.fill((0, 0, 0, 0));
                last_update_time = now
                snake = snake.move(direction)
                snake.draw_snake(SNAKE_LAYER, SNAKE_COLOR, SNAKE_WIDTH, SPRITE_IMAGE)
                
                # Check if snake hit borders
                if snake.x >= 800 or snake.x < 0 or snake.y >= 800 or snake.y < 0:
                    game_state = "over"

                # Check if snake hit itself
                if snake.checkCollide():
                    game_state = "over"
                
                if (snake.x == food.x and snake.y == food.y):
                    FOOD_LAYER.fill((0, 0, 0, 0))
                    food.respawn(snake)
                    food.drawFood(FOOD_LAYER, FOOD_COLOR)
                    SCORE += 1
                    print("Score: {}".format(SCORE))
                    snake.increase_size()

        elif game_state == "over":
            background.fill((0, 0, 0, 0))
            SNAKE_LAYER.fill((0, 0, 0, 0))
            FOOD_LAYER.fill((0, 0, 0, 0))
            image_surface = pygame.image.load("assets\game_over_screen.jpg")
            image_surface = pygame.transform.scale(image_surface, (HEIGHT, WIDTH))
            background.blit(image_surface, (0, 0))

        elif game_state == "home screen":
            image_surface = pygame.image.load("assets\home-screen.jpg")
            image_surface = pygame.transform.scale(image_surface, (HEIGHT, WIDTH))
            background.blit(image_surface, (0, 0))

        # Update Layers
        Window.blit(background, (0, 0))
        Window.blit(FOOD_LAYER, (0, 0))
        Window.blit(SNAKE_LAYER, (0, 0))
        pygame.display.update()
        
    pygame.quit()

main()