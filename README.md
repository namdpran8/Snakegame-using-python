# Snakegame-using-python

### Description of the Snake Game Program

This program implements a classic Snake game using the Turtle graphics module in Python. The game includes a welcome screen, gameplay mechanics, scoring, and an ending screen when the snake bites itself. Below is a detailed description of the components and functionalities of the program.

#### Components

1. **Welcome Screen**:
    - Displays a welcome message and instructions to start the game.
    - The game starts when the player presses the spacebar.

2. **Game Setup**:
    - The game window is set up with a specific width and height.
    - The background color of the window is set to black.
    - The `screen.tracer(0)` is used to control manual updates to reduce flickering.

3. **Snake and Food**:
    - The snake is represented by a series of circles.
    - The food is a red circle that appears at random positions on the screen.
    - The snake moves in a specified direction and grows when it eats the food.
    - The game allows screen wrapping, meaning the snake can move off one edge of the screen and reappear on the opposite edge.

4. **Score Display**:
    - The score is displayed at the top of the screen.
    - The score increases by 10 points each time the snake eats the food.
    - The `update_score` function updates the score display without causing flickering.

5. **Game Mechanics**:
    - The snake moves continuously in the current direction.
    - The player can change the direction of the snake using the arrow keys.
    - The game checks for collisions with itself, which results in the game ending.

6. **Ending Screen**:
    - Displays a game over message and the player's score when the snake bites itself.
    - Provides instructions to restart the game by pressing the spacebar.

#### Functions

- **show_welcome_screen**: Displays the welcome screen with instructions.
- **start_game**: Clears the welcome screen and starts the game by setting up the necessary components.
- **setup_game**: Initializes the game components, including the snake, food, and score display.
- **reset**: Resets the game state, including the snake's initial position, direction, food position, and score.
- **move_snake**: Handles the movement of the snake, checks for collisions, updates the screen, and schedules the next movement.
- **food_collision**: Checks if the snake has eaten the food and updates the food position and score if true.
- **get_random_food_pos**: Returns a random position within the screen boundaries for the food.
- **get_distance**: Calculates the distance between two points.
- **go_up, go_right, go_down, go_left**: Functions to change the snake's direction based on user input.
- **draw_snake**: Draws the snake on the screen by stamping the turtle shape at each segment's position.
- **update_score**: Updates the score display on the screen.
- **end_game**: Displays the game over screen with the final score and instructions to restart the game.

#### How to Play

1. Run the program.
2. The welcome screen appears with the message "Welcome to Snake Game! Press 'Space' to start".
3. Press the spacebar to start the game.
4. Use the arrow keys to control the direction of the snake:
   - Up arrow to move up.
   - Down arrow to move down.
   - Left arrow to move left.
   - Right arrow to move right.
5. The snake moves continuously, eating food to grow and increasing the score.
6. If the snake bites itself, the game ends, and a game over screen appears displaying the final score and instructions to restart the game.
7. Press the spacebar to restart the game from the welcome screen.

This program provides a basic but complete implementation of the Snake game, with features for starting, playing, and ending the game, along with score tracking and display.
