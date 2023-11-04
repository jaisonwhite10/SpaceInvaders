from turtle import Turtle,Screen
import time


class Spaceship(Turtle):

    def __init__(self, position):
        super().__init__()
        # self.shape('images/ship.gif')
        self.shape("circle")
        self.color('white')
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def shoot_lazer(self):
        lazer = Turtle()
        screen = Screen()
        lazer.shape()
        lazer.setheading(90)
        lazer.color("white")
        lazer.penup()
        lazer.speed("fastest")
        lazer.goto(self.xcor(), self.ycor())

        def move_laser():
            lazer_new_y = lazer.ycor() + 10
            lazer.goto(lazer.xcor(), lazer_new_y)
            screen.ontimer(move_laser, 50)

        move_laser()

