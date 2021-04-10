import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtler")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkey


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()



exitonclick = screen.exitonclick()