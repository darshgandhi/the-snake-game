# Snake Game

A classic Snake game implementation using Python and Pygame.

## Overview

This Snake Game is a modern implementation of the classic arcade game. The player controls a snake that moves around the screen, eating food to grow longer. The game ends if the snake collides with itself or the boundaries of the playing field.

## Features

- Smooth snake movement with proper sprite transitions for turns, straight body segments, and tail
- Visual feedback with custom sprites for different parts of the snake
- Dynamic growth when the snake eats food
- Collision detection to prevent the snake from moving through itself
- Score tracking based on food collected

## Requirements

- Python 3.6 or higher
- Pygame library

## How to Run

Simply run the main Python script:

```
python main.py
```

Or use your preferred Python IDE (like PyCharm, VSCode, or IDLE) and click the "Run" button after opening the main script.

## How to Play

- Use the arrow keys to control the snake's direction
- Collect food to grow longer and increase your score
- Avoid colliding with yourself or the boundaries
- Try to achieve the highest score possible!

## Code Structure

- `main.py`: Entry point for the game, handles the game loop and event processing
- `snake.py`: Contains the Snake class that manages the snake's movement, growth, and display
- Assets are loaded directly into the game for simplicity

## Snake Class

The Snake class is the core component of the game, responsible for:

- Managing the linked list of snake segments
- Handling movement and direction changes
- Drawing the snake with appropriate sprites for head, body turns, straight segments, and tail
- Collision detection
- Growing the snake when food is eaten

## Controls

- Up Arrow: Move snake up
- Down Arrow: Move snake down
- Left Arrow: Move snake left
- Right Arrow: Move snake right
- ESC: Quit game (if implemented)

## Game Mechanics

- The snake moves continuously in the current direction
- The snake grows when it eats food
- The game ends if the snake hits itself or the boundaries
- Score increases each time food is collected

## Customization

You can customize the game by editing constants in the main script:
- Change game speed
- Modify colors and visual elements
- Adjust the game board size

## Credits

This game was created using Pygame, a set of Python modules designed for writing video games.
