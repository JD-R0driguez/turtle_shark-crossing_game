from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    """
    ScoreBoard inheres from Turtle class. It keeps track of the score and the game status.
    Updates when the player gains a level and when the player collides with a shark
    """
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0

    def update_board(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"level: {self.score}", align="left", font=FONT)

    def level_up(self):
        self.score += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
