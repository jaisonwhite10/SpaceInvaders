from turtle import Turtle, Screen
from scoreboard import Scoreboard
import schedule
import random
import time


class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.x_positions = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
        self.y_positions = [30, 70, 110, 150, 190]
        self.list_of_enemies = [[], [], [], [], []]
        self.moving_speed = 0.3
        self.laser = None
        self.invaders = []

    def create_alien(self, jellyfish_image, crab_image, squid_image):
        for alien_y in range(0, 5):
            for alien_index in range(0, 11):
                alien = Aliens()
                alien.goto(self.x_positions[alien_index], self.y_positions[alien_y])
                self.invaders.append(alien)
                self.list_of_enemies[alien_y].append(alien)

        for alien in self.list_of_enemies[0]:
            alien.shape(jellyfish_image)
        for alien in self.list_of_enemies[1]:
            alien.shape(jellyfish_image)
        for alien in self.list_of_enemies[2]:
            alien.shape(crab_image)
        for alien in self.list_of_enemies[3]:
            alien.shape(crab_image)
        for alien in self.list_of_enemies[4]:
            alien.shape(squid_image)



    def create_alien_ship(self, image):
        alien = Aliens()
        screen = Screen()
        alien.shape(image)
        alien.goto(0, y=270)
        alien.move_ship()

    def move_ship(self):

        # screen = Screen()
        self.setheading(0)
        self.speed('slowest')
        self.forward(self.moving_speed)


    def move_down(self):

        self.setheading(270)
        self.forward(2)

    def move_aliens(self):

        for list in self.list_of_enemies:

            for alien in list:
                alien.forward(1)
            self.check_borders()

    def increase_speed(self, alien):
        alien.moving_speed += 0.1

    def check_borders(self):

        for list in self.list_of_enemies:
            right_screen = any(alien.xcor() > 370 for alien in list)
            left_screen = any(alien.xcor() < -370 for alien in list)
            for alien in list:
                if right_screen:
                    alien.move_down()
                    alien.setheading(180)
                    alien.increase_speed(alien)
                elif left_screen:
                    alien.move_down()
                    alien.setheading(0)
                    alien.increase_speed(alien)


    def shoot_laser(self):
        self.laser = Turtle()
        screen = Screen()
        self.laser.shapesize(0.5, 1)
        self.laser.setheading(270)
        self.laser.color("white")
        self.laser.penup()
        self.laser.speed("slow")
        self.laser.goto(self.xcor(), self.ycor())
        self.move_laser()


    def move_laser(self):
        screen = Screen()
        laser_new_y = self.laser.ycor() - 5
        self.laser.goto(self.laser.xcor(), laser_new_y)

        screen.ontimer(self.move_laser, 100)

    def alien_shoot(self):
        random_list = random.choice([sublist for sublist in self.list_of_enemies])
        random_alien = random.choice(random_list)
        random_alien.shoot_laser()

    def aliens_win(self):
        turtle = Turtle()
        turtle.color('white')
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(0, 0)
        turtle.write('You Lose', align='center', font=('Courier', 20, 'normal'), move=False)

