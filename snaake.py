import turtle
import random

WIDTH = 500
HEIGHT = 500
FOOD_SIZE = 10
DELAY = 100

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# Initialize score
score = 0

def show_welcome_screen():
    screen.clear()
    screen.bgcolor("black")
    welcome_turtle = turtle.Turtle()
    welcome_turtle.color("white")
    welcome_turtle.penup()
    welcome_turtle.hideturtle()
    welcome_turtle.write("Welcome to Snake Game!\nPress 'Space' to start",
                         align="center", font=("Arial", 24, "normal"))
    screen.update()
    screen.listen()
    screen.onkey(start_game, "space")

def start_game():
    screen.clear()
    screen.bgcolor("black")
    setup_game()
    reset()

def setup_game():
    global pen, food, score_display
    pen = turtle.Turtle("circle")  # Pen (now circles)
    pen.penup()
    pen.color("yellow")

    food = turtle.Turtle()  # Food
    food.shape("circle")
    food.color("red")
    food.shapesize(FOOD_SIZE / 20)  # Default size of turtle "square" shape is 20.
    food.penup()

    score_display = turtle.Turtle()  # Score display
    score_display.penup()
    score_display.color("white")
    score_display.goto(0, HEIGHT // 2 - 20)
    score_display.hideturtle()

    screen.listen()  # Event handlers
    screen.onkey(go_up, "Up")
    screen.onkey(go_right, "Right")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")

def reset():
    global snake, snake_direction, food_pos, score
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    score = 0
    update_score()
    move_snake()

def move_snake():
    global snake_direction, score

    # Next position for head of snake
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check self-collision
    if new_head in snake[:-1]:
        end_game()
    else:
        snake.append(new_head)
        if not food_collision():
            snake.pop(0)

        # Allow screen wrapping
        if abs(snake[-1][0]) > WIDTH / 2 or abs(snake[-1][1]) > HEIGHT / 2:
            snake[-1][0] %= WIDTH
            snake[-1][1] %= HEIGHT

        pen.clearstamps()
        draw_snake()
        update_score()  # Update the score display
        screen.update()
        screen.tracer(0)
        turtle.ontimer(move_snake, DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        score += 10  # Increase score
        return True
    return False

def get_random_food_pos():
    x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def draw_snake():
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

def update_score():
    screen.tracer(0)  # Turn off automatic screen updates
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
    screen.update()  # Manually update the screen
    screen.tracer(1)  # Turn on automatic screen updates

def end_game():
    screen.clear()
    screen.bgcolor("black")
    end_turtle = turtle.Turtle()
    end_turtle.color("white")
    end_turtle.penup()
    end_turtle.hideturtle()
    end_turtle.write(f"Game Over!\nYour Score: {score}\nPress 'Space' to restart",
                     align="center", font=("Arial", 24, "normal"))
    screen.update()
    screen.listen()
    screen.onkey(start_game, "space")

screen = turtle.Screen()  # Screen
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)  # Turn off automatic animation

show_welcome_screen()

turtle.done()
