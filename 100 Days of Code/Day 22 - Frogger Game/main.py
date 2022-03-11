import time
from turtle import Screen, onkeypress
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=1280, height=720)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # Detect turtle collision with any car.
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

        # Detect if player has reached the top and speed up cars.
        if player.ycor() == 280:
            player.finish()
            car.speed_up()
            score.level_up()

screen.exitonclick()
