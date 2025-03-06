import pygame

class Snake:
    def __init__(self, x, y, direction, image) -> None:
        self.x = x
        self.y = y
        self.direction = direction
        self.image = image
        self.next = None
    
    def get_image(self, sheet, width, height, sprite_x, sprite_y, cell_xy):
        sprite_image = pygame.Surface((cell_xy, cell_xy), pygame.SRCALPHA).convert_alpha()
        sprite_image.blit(sheet, (0, 0), (sprite_x, sprite_y, cell_xy, cell_xy))
        sprite_image = pygame.transform.scale(sprite_image, (width, height))
        return sprite_image

    def move(self, direction):
        if direction == 'up':
            new_segment = Snake(self.x, self.y-80, direction, direction)
        elif direction == 'down':
            new_segment = Snake(self.x, self.y+80, direction, direction)
        elif direction == 'left':
            new_segment = Snake(self.x-80, self.y, direction, direction)
        else:
            new_segment = Snake(self.x+80, self.y, direction, direction)
        
        new_segment.next = self

        # REMOVE LAST
        curr = new_segment
        prev = None
        while curr.next is not None:
            prev = curr
            curr = curr.next
        
        prev.next = None

        return new_segment
    
    def draw_snake(self, layer, color, SNAKE_WIDTH, SPRITE_IMAGE):
        curr = self
        
        # First, handle the head (first segment)
        if curr.direction == 'up':
            snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 192, 0, 64)
        elif curr.direction == 'right':
            snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 256, 0, 64)
        elif curr.direction == 'down':
            snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 256, 64, 64)
        elif curr.direction == 'left':
            snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 192, 64, 64)
        
        layer.blit(snake_image, (curr.x, curr.y))
        
        # Then process the body segments
        prev = curr
        curr = curr.next
        
        while curr:
            if curr.next is None:  # Tail
                if prev.direction == 'up':
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 192, 128, 64)
                elif prev.direction == 'right':
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 256, 128, 64)
                elif prev.direction == 'down':
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 256, 192, 64)
                elif prev.direction == 'left':
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 192, 192, 64)
            elif prev.direction == curr.direction:  # Straight Body
                if curr.direction in ['up', 'down']:
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 128, 64, 64)
                else:  # Left/Right
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 64, 0, 64)
            else:  # Turns - based on previous and current direction
                if (prev.direction == 'up' and curr.direction == 'right') or (prev.direction == 'left' and curr.direction == 'down'):
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 128, 128, 64)
                elif (prev.direction == 'up' and curr.direction == 'left') or (prev.direction == 'right' and curr.direction == 'down'):
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 0, 64, 64)
                elif (prev.direction == 'down' and curr.direction == 'right') or (prev.direction == 'left' and curr.direction == 'up'):
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 128, 0, 64)
                elif (prev.direction == 'down' and curr.direction == 'left') or (prev.direction == 'right' and curr.direction == 'up'):
                    snake_image = self.get_image(SPRITE_IMAGE, SNAKE_WIDTH, SNAKE_WIDTH, 0, 0, 64)

            layer.blit(snake_image, (curr.x, curr.y))
            prev = curr
            curr = curr.next
    
    def increase_size(self):
        # Find the tail
        curr = self
        while curr.next is not None:
            curr = curr.next
            
        # Add a new segment at the tail position based on tail direction
        if curr.direction == 'up':
            new_segment = Snake(curr.x, curr.y+80, curr.direction, curr.direction)
        elif curr.direction == 'down':
            new_segment = Snake(curr.x, curr.y-80, curr.direction, curr.direction)
        elif curr.direction == 'left':
            new_segment = Snake(curr.x+80, curr.y, curr.direction, curr.direction)
        else:  # right
            new_segment = Snake(curr.x-80, curr.y, curr.direction, curr.direction)
            
        curr.next = new_segment

    def get_direction(self):
        return self.direction

    def checkCollide(self):
        return self.checkInBody(self.x, self.y)
    
    def checkInBody(self, x, y):
        curr = self.next  # Start checking from the second segment
        while curr is not None:
            if curr.x == x and curr.y == y:
                return True
            curr = curr.next
        return False