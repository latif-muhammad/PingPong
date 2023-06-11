from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 0.15
        self.y_move = 0.15

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = - self.y_move

    def bounce_x(self):
        self.x_move = - self.x_move

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
