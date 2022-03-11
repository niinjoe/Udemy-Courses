from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gamemenu import GameMenu
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
gamemenu = GameMenu()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
# screen.onkey(gamemenu)

# gamemenu.menu()
# gamemenu.select_option()


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.collect()

    # Detect collision with wall.
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        scoreboard.game_over()
        game_on = False

    # Detect collision with body.
    # If head collides with any segment, trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
