from turtle import Turtle,Screen
screen = Screen()

class MysteryShip(Turtle):

    def __init__(self,shape):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.moving_speed = 0.5
        self.shape(shape)
        self.goto(1500,270)


    def move_ship(self):
        self.setheading(180)
        self.speed('slowest')
        self.forward(0.5)
        if self.xcor() < -1500:
            self.hideturtle()
            self.goto(1500,270)
            self.showturtle()

