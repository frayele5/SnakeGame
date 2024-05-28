from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.move()

    def move(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

