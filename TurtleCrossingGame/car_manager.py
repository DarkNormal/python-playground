from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.active_cars = []

    def create_car(self):
        rand = random.randint(0,6)
        if rand == 0:
            car = Car(color=COLORS[random.randint(0, len(COLORS) - 1)], speed=self.move_speed)
            self.active_cars.append(car)

    def move_cars(self):
        for car in self.active_cars:
            car.move()

    def check_collision(self, turtle_coords):
        pass

    def check_cars(self):
        for car in self.active_cars:
            if car.xcor() < -340:
                self.reset_car(car)

    def reset_car(self, car):
        car.hideturtle()
        car.goto((320, random.randint(-300, 300)))
        car.showturtle()

    def increment_difficulty(self):
        self.move_speed += MOVE_INCREMENT
        for car in self.active_cars:
            car.move_speed = self.move_speed

    def detect_collision(self, player1):
        for car in self.active_cars:
            if car.distance(player1) <= 20:
                return True
        return False
