from turtle import Turtle

class Aliens(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.x_positions = [-250,-200,-150,-100,-50,0,50,100,150,200,250]
        self.list_of_enemies = [[],[],[],[],[]]


    def create_alien(self, image, y_coord,enemy_index):

        for alien_index in range(0, 11):
            alien = Aliens()
            alien.shape(image)
            alien.goto(self.x_positions[alien_index], y_coord)
            self.list_of_enemies[enemy_index].append(alien)

    def create_alien_ship(self,image,ycoord):
        alien = Aliens()
        alien.shape(image)
        alien.goto(0,ycoord)
    # def move_aliens(self):
    #
    #     for list in self.list_of_enemies:
    #         # max_alien = max(list, key=lambda alien: alien.xcor())
    #         # min_alien = min(list, key=lambda alien: alien.xcor())
    #         # if max_alien.xcor() > 270:
    #         #     for alien in list:
    #         #         self.move_left(alien)
    #         # elif min_alien.xcor() < -270:
    #         #     for alien in list:
    #         #         self.move_right(alien)
    #
    #         ###mine
    #         list_of_x_coordinate = [alien.xcor() for alien in list]
    #         max_x = max(list_of_x_coordinate)
    #         min_x = min(list_of_x_coordinate)
    #         for alien in list:
    #             self.move_right(alien)
    #         #     # max_x = alien.xcor().max()
    #         #     # self.move_left(alien)
    #             if max_x > 270:
    #                 self.move_left(alien)
    #             elif min_x < -270:
    #                 self.move_right(alien)
    #
    #
    #         # ###mine

    def move_aliens(self):
        for list in self.list_of_enemies:
            # list_of_x_coordinate = [alien.xcor() for alien in list]
            # max_x = max(list_of_x_coordinate)
            # min_x = min(list_of_x_coordinate)
            for alien in list:
                alien.forward(0.1)
            self.check_borders()




    def check_borders(self):

        for list in self.list_of_enemies:

            right_screen = any(alien.xcor() > 370 for alien in list)
            left_screen = any(alien.xcor() < -370 for alien in list)
            for alien in list:
                if right_screen:
                    alien.setheading(180)
                elif left_screen:
                    alien.setheading(0)










