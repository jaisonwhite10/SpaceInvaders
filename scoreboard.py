from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-70, -380)
        self.write(f'score: {self.score}', align='right', font=('Courier', 20, 'normal'), move=False)
        self.goto(-250, -380)
        self.write(f'lives: {self.lives}', align='right', font=('Courier', 20, 'normal'), move=False)

    def increase_score(self, score):
        self.score += int(score)
        self.update_scoreboard()


    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def aliens_won(self):
        self.goto(0,0)
        self.write('You Lose', align='center', font=('Courier', 20, 'normal'), move=False)
        self.goto(0,-30)
        self.write('(Restart App To Play Again!)', align='center', font=('Courier', 20, 'normal'), move=False)

    def player_won(self):
        self.goto(0, 0)
        self.write('You Won!', align='center', font=('Courier', 20, 'normal'), move=False)
        self.goto(0, -30)
        self.write('(Restart App To Play Again!)', align='center', font=('Courier', 20, 'normal'), move=False)




