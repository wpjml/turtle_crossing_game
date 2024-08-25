import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

    def level_write(self):
        self.speed("fastest")
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
