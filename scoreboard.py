from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_board()

    def update_board(self):
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_scored(self):
        self.clear()
        self.l_score += 1
        self.update_board()

    def r_scored(self):
        self.clear()
        self.r_score += 1
        self.update_board()

    def endGame(self):
        if self.r_score == 2 or self.l_score == 2:
            self.goto(0, 40)
            if self.r_score == 2:
                self.write("Right player won", align="center", font=("Courier", 20, "normal"))
            else:
                self.write("Left player won", align="center", font=("Courier", 20, "normal"))
            return True

        return False
