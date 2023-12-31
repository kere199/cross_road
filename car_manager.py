from turtle import Turtle 
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.counter = 0
        self.speed = 5


    def move_cars(self):
        for car in self.cars:
            car.setx(car.xcor() - self.speed)
            self.counter += 1

    def increase_speed(self):
        self.speed += 5



    def generate_cars(self):
        if self.counter % 10 == 0:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_position = random.randint(-240, 240)
            car.goto(300, y_position)
            self.cars.append(car)


    def check_collision(self,player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False
       
    


        
        


    
        
