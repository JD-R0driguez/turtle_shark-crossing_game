from turtle import Screen
from player import Player
from shark_controller import SharkController
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
# tracer turns screen animation off
screen.tracer(0)


score = Scoreboard()
score.update_board()

player = Player()
screen.onkeypress(player.move_forward, "Up")
screen.listen()
shark_control = SharkController()

game_on = True
while game_on:

    time.sleep(0.1)
    shark_control.create_skarK_pack()
    shark_control.pack_movement()
    screen.update()
    for shark in shark_control.shark_pack:
        if player.distance(shark.head) < 30:
            score.game_over()
            game_on = False
    if player.crossed_screen():
        player.starting_position()
        shark_control.speed_increase()
        score.level_up()

screen.exitonclick()
