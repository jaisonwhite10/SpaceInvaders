from turtle import Turtle,Screen
from aliens import Aliens
import time

aliens = Aliens()
class Spaceship(Turtle):

    def __init__(self, position):
        super().__init__()
        # self.shape('images/ship.gif')
        self.shape("circle")
        self.color('white')
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.laser = None


    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def shoot_laser(self):
        laser = Turtle()
        self.laser = laser
        screen = Screen()
        laser.shapesize(0.5,1)
        laser.setheading(90)
        laser.color("white")
        laser.penup()
        laser.speed("fastest")
        laser.goto(self.xcor(), self.ycor())

        

        #defining move_laser() leads to better shooting gameplay than when I call self.move_laser() in the shoot_laser function, also keeping laser as laser not self.laser
        def move_laser():
            laser_new_y = laser.ycor() + 10
            laser.goto(laser.xcor(), laser_new_y)
            # self.detect_laser_collision(laser)
            # if laser.distance() < 30:
            #     print('hit')
            # if self.detect_laser_collision(laser,alien_list):
            #     print('alien hit')
            # self.detect_laser_collision(laser)

            screen.ontimer(move_laser, 50)
        move_laser()


    def laser(self):
        if self.laser:
            print('true')
        else:
            print('no laser')

    def detect_laser_collision(self,laser,alien):
        if laser.distance(alien) < 30:
            print('hit')













