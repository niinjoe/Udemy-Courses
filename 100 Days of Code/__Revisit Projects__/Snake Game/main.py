from turtle import Screen

from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.screensize(600, 600)
screen.listen()

snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.tracer(0.1)
    snake.move_snake()
    

screen.exitonclick()
