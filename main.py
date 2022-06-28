import time
from turtle import Screen
from player import Player
from car_manage import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player_one = Player()
score_board = Scoreboard()

screen.listen()
screen.onkey(player_one.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player_one) < 20:
            game_is_on = False
            score_board.game_over()

    if player_one.ycor() > 280:
        player_one.reset()
        car_manager.level_up()
        score_board.increase_level()


screen.exitonclick()
