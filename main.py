import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player = Player()
scoreboard = Scoreboard()
# scoreboard.print_level()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move_up, "Up")
scoreboard.print_level()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor()>250:
        player.return_back()
        scoreboard.increase_level()



