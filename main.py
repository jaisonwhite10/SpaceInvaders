from turtle import Turtle, Screen
from spaceship import Spaceship
from tkinter import *

#adds ship image to Turtle Screen
ship_image = "images/ship.gif"

screen = Screen()

#adds spaceship image to Screen
screen.addshape(ship_image)

## Creates a ship and sets it at the defined x,y coordinates
ship = Spaceship((0,-220))

#adds ship image to spaceship Turtle
ship.shape(ship_image)

screen.bgcolor("black")
screen.setup(width=700,height=700)
screen.title('Space Invaders')
screen.tracer(0)
screen.listen()


screen.onkeypress(fun=ship.move_right,key="Right")
screen.onkeypress(fun=ship.move_left,key="Left")
screen.onkeypress(fun=ship.shoot_lazer,key='space')



while True:
    screen.update()



