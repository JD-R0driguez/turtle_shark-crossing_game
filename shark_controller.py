from shark import Shark
import random

COLORS = ["midnight blue", "silver", "light steel blue", "cornflower blue",
          "royal blue", "dodger blue", "sky blue", "steel blue"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class SharkController:
    """
    SharkController manages the all the shark instances. It defines the shark's colors and relative
    position in the screen, as well as the shark peace once the player increase a level.
    """
    def __init__(self):
        self.shark_pack = []
        self.pack_speed = STARTING_MOVE_DISTANCE


    def create_skarK_pack(self):
        # Every 0.1 secs we call this function in the main.py. We define a random int (kind of like
        # throwing a die) to randomize the instance of a shark object.
        random_sharks = random.randint(1, 6)
        if random_sharks == 1:
            y_pos = random.randint(-220, 220)
            shark = Shark(self.pack_speed)
            color = random.choice(COLORS)
            shark.change_color(color)
            shark.goto_pos(300, y_pos)
            self.shark_pack.append(shark)


    def pack_movement(self):
        for shark in self.shark_pack:
            shark.move_x()

    def speed_increase(self):
        for shark in self.shark_pack:
            new_shark_speed = shark.pace + MOVE_INCREMENT
            shark.pace = new_shark_speed
            self.pack_speed = new_shark_speed