import random
import turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car = []
        self.move_speed = STARTING_MOVE_DISTANCE
        for _ in range(20):
            car = turtle.Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.goto(random.randint(0, 800), random.randint(-250, 280))
            car.color(random.choice(COLORS))
            car.setheading(180)
            self.car.append(car)

    def move_car(self):
        for car in self.car:
            if car.xcor() < -300:
                new_x = random.randint(320, 500)
                new_y = random.randint(-250, 250)
                car.goto(new_x, new_y)
            car.forward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
