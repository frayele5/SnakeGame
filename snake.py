from turtle import Turtle

# Define your snake game logic here
MOVE_DISTANT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        self.tail = self.turtles[-1]
        self.speed_move = 0.2

    def create_snake(self):
        for i in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.speed("fastest")
            self.turtles.append(tim)

        tmp = self.turtles[0].heading()
        for i in range(1, len(self.turtles)):
            self.turtles[i].up()
            self.turtles[i].setx(tmp - MOVE_DISTANT)
            tmp = self.turtles[i].xcor()

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            temp_x = self.turtles[i - 1].xcor()
            temp_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(temp_x, temp_y)
        self.head.up()
        self.head.forward(MOVE_DISTANT)

    def grow(self, x, y):
        tim = Turtle("square")
        tim.speed("fastest")
        tim.up()
        tim.color("white")
        tim.goto(x, y)
        self.turtles.append(tim)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)