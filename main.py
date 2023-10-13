import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.listen()
screen.onkeypress(player.move_up, "Up")
scoreboard.print_level()
carmanager = CarManager()

carspeed = 5
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.move_cars(carspeed)
    carmanager.generate_cars()
    if player.ycor()>250:
        player.return_back()
        scoreboard.increase_level()





