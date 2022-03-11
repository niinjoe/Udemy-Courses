from hashlib import new
from tkinter.constants import S
from turtle import Turtle
from random import choice, randrange, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        dice = randint(1, 6)
        # "dice" controls amount of cars generated in the map.
        if dice == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.goto(randrange(590, 600, 20), randrange(-300, 300, 20))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
