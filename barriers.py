from turtle import Turtle

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.all_barriers = []
        self.x_coordinates = [-330,-130,70,270]

    def barriers(self):
        self.y = -200
        for x in self.x_coordinates:
            self.x = x
            for length in range(10):
                for width in range(10):
                    brick = Bricks()
                    brick.color('white')
                    brick.shape('square')
                    brick.shapesize(0.5, 0.5)
                    brick.goto(self.x,self.y)
                    self.all_barriers.append(brick)
                    self.x += 10
                self.y += 10
                self.x = x
            self.y = -200


    def destroy_brick(self,laser):
        for brick in self.all_barriers:
            if laser.isvisible() and brick.isvisible():
                if laser.distance(brick) < 20:
                    brick.hideturtle()
                    laser.hideturtle()
                    self.all_barriers.remove(brick)