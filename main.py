from turtle import Turtle, Screen
from spaceship import Spaceship
from aliens import Aliens
from tkinter import *

#adds ship image to Turtle Screen
ship_image = "images/ship.gif"

jelly_fish_image = "images/jelly_fish.gif"

crab_alien_image = "images/crab_alien3.gif"

squid_alien_image = "images/squid_alien.gif"

alien_ship_image = "images/alien_ship.gif"
screen = Screen()

#adds spaceship image to Screen
screen.addshape(ship_image)
screen.addshape(jelly_fish_image)
screen.addshape(crab_alien_image)
screen.addshape(squid_alien_image)
screen.addshape(alien_ship_image)
## Creates a ship and sets it at the defined x,y coordinates
ship = Spaceship((0,-250))

#adds ship image to spaceship Turtle
ship.shape(ship_image)

alien = Aliens()
#Jellyfish Aliens
alien.create_alien(image=jelly_fish_image,y_coord=30,enemy_index=0)
alien.create_alien(image=jelly_fish_image,y_coord=70,enemy_index=1)

#Crab Aliens
alien.create_alien(image=crab_alien_image,y_coord=110,enemy_index=2)
alien.create_alien(image=crab_alien_image,y_coord=150,enemy_index=3)

#Jellyfish Alien
alien.create_alien(image=squid_alien_image,y_coord=190,enemy_index=4)

#Alien Ship
alien.create_alien_ship(image=alien_ship_image,ycoord=270)






screen.bgcolor("black")
screen.setup(width=800,height=800)
screen.title('Space Invaders')
screen.tracer(0)
screen.listen()


screen.onkeypress(fun=ship.move_right,key="Right")
screen.onkeypress(fun=ship.move_left,key="Left")
screen.onkeypress(fun=ship.shoot_lazer,key='space')



while True:
    alien.move_aliens()
    screen.update()



