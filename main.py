from turtle import Turtle, Screen
from spaceship import Spaceship
from aliens import Aliens
from scoreboard import Scoreboard
from mystery_ship import MysteryShip
from barriers import Bricks
from tkinter import *
import schedule
import time

# adds gif images to Turtle Screen
ship_image = "images/ship.gif"
jelly_fish_image = "images/jelly_fish.gif"
crab_alien_image = "images/crab_alien3.gif"
squid_alien_image = "images/squid_alien.gif"
alien_ship_image = "images/alien_ship.gif"

scoreboard = Scoreboard()

screen = Screen()

turtle = Turtle()
# adds images to Screen
screen.addshape(ship_image)
screen.addshape(jelly_fish_image)
screen.addshape(crab_alien_image)
screen.addshape(squid_alien_image)
screen.addshape(alien_ship_image)
## Creates a ship and sets it at the defined x,y coordinates
ship = Spaceship((0, -300))

# adds ship image to spaceship Turtle
ship.shape(ship_image)

alien = Aliens()
alien.create_alien(jelly_fish_image, crab_alien_image, squid_alien_image)

mystery_ship = MysteryShip(alien_ship_image)

barriers = Bricks()
barriers.barriers()

screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title('Space Invaders')
screen.tracer(0)
screen.listen()

screen.onkeypress(fun=ship.move_right, key="Right")
screen.onkeypress(fun=ship.move_left, key="Left")
screen.onkeypress(ship.shoot_laser, 'space')

schedule.every(5).seconds.do(alien.alien_shoot)

game_is_on = True
while game_is_on:
    screen.update()
    #runs the schedules function making aliens shoot every 5 seconds but once a winner has been chosen
    # the list of aliens is emptied which causes an IndexError
    try:
        schedule.run_pending()
    except IndexError:
        continue
    alien.move_aliens()
    mystery_ship.move_ship()

    # Detects Mystery Ship being hit by ship laser
    if mystery_ship.isvisible() and ship.laser:
        if ship.laser.distance(mystery_ship) < 20 and ship.laser.isvisible():
            mystery_ship.hideturtle()
            scoreboard.increase_score(300)
            ship.laser.hideturtle()

    if ship.laser:
        barriers.destroy_brick(ship.laser)

    for sublist in alien.list_of_enemies:
        for aliens in sublist:
            #Detects the distance between ship and aliens
            if ship.isvisible():
                if ship.distance(aliens) < 30:
                    screen.clear()
                    screen.bgcolor('black')
                    alien.list_of_enemies = []
                    scoreboard.aliens_won()
                    game_is_on = False
                    break

            if ship.laser:
                # if the laser fired by the ship hits an alien increases score by 100, and remove alien from list
                if ship.laser.distance(aliens) < 20 and ship.laser.isvisible():
                    aliens.hideturtle()
                    ship.laser.hideturtle()
                    sublist.remove(aliens)
                    scoreboard.increase_score(100)

            # if alien laser hits ship decrease life and respawn player
            if aliens.laser:
                if aliens.laser.distance(ship) < 20 and aliens.laser.isvisible():
                    ship.hideturtle()
                    scoreboard.decrease_lives()
                    time.sleep(0.3)
                    ship.goto(0, -300)
                    time.sleep(0.5)
                    ship.showturtle()

                barriers.destroy_brick(aliens.laser)

    if scoreboard.score >= 5500:
        screen.clear()
        screen.bgcolor('black')
        alien.list_of_enemies = []
        scoreboard.player_won()

    if scoreboard.lives > 0:
        game_is_on = True
    else:
        game_is_on = False

    screen.update()
