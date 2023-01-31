from turtle import Turtle

# Dictionary with shark attributes. Each "body_part" is a list with:
# coordinates (x, y), orientation, width stretch, length stretch, and shape.
# e.g.: "head": coordinates = (0, 0), orientation = 180,
# width stretch = 1.3, length stretch = 2.5, and shape = "triangle"
BODY_COMPONENTS = {
                    "head": [(0, 0), 180, 1.3, 2.5, "triangle"],
                    "body": [(40, 0), 0, 1.4, 5, "triangle"],
                    "mouth": [(0, -6), 190, 1, 1.5, "triangle"],
                    "fin": [(18, 17), 80, 1, 1.6, "triangle"],
                    "l_fin": [(58, 7), 80, 0.5, 0.5, "triangle"],
                    "b_fin": [(38, -8), 290, 0.6, 0.6, "triangle"],
                    "tail": [(90, 0), 185, 4, 2, "classic"]
                    }


class Shark:
    """
    The Shark class uses the turtle module to bring a super sleek shark object to live. The class uses
    its own methods for axial movements and for color allocation.
    """
    def __init__(self, pace):
        self.pace = pace
        self.shark_body = []
        self.create_body()
        self.head = self.shark_body[0]


    def create_body(self):
        for body_part in BODY_COMPONENTS.values():
            self.create_part(body_part)

    # Create the shark's body with Turtle instances and the attributes from BODY_COMPONENTS
    def create_part(self, part_traits):
        part = Turtle(part_traits[4])
        part.penup()
        part.goto(part_traits[0])
        part.setheading(part_traits[1])
        part.shapesize(stretch_wid=part_traits[2], stretch_len=part_traits[3])
        self.shark_body.append(part)

    def change_color(self, color):
        for body_part in self.shark_body:
            body_part.color(color)

    def move_x(self):
        for body_part in self.shark_body:
            new_x = body_part.xcor()
            new_x -= self.pace
            body_part.setx(new_x)

    def move_y(self):
        for body_part in self.shark_body:
            new_y = body_part.ycor()
            new_y -= self.pace
            body_part.sety(new_y)

    def goto_pos(self, x_pos, y_pos):
        for body_part in self.shark_body:
            new_x = body_part.xcor()
            new_y = body_part.ycor()
            new_x += x_pos
            new_y += y_pos
            body_part.goto(new_x, new_y)

    def shark_xcor(self):
        return self.head.xcor()

    def shark_ycor(self):
        return self.head.ycor()
