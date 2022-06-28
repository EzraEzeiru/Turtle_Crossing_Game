from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-240, 270)
        self.hideturtle()
        self.write(arg=f"Level: {self.level}", align= "center", font=FONT)


    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        end_game = Turtle()
        end_game.color("black")
        end_game.write(arg="GAME OVER", align="center", font=("Courier", 50, "normal"))

