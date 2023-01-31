from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# The player class control all the aspects related to the player behaviour such as movement, position,
# and status (reaching the end of the screen)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.starting_position()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def crossed_screen(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False


