class Car():
    def __init__(self, brand, car_model, current_speed):
        self.brand = brand
        self.car_model = car_model
        self.current_speed = current_speed

    def accelerate(self, speed_accelerated):
        self.current_speed += speed_accelerated

    def brake(self, reduced_speed):
        self.current_speed -= reduced_speed

    def __str__(self):
        return f'The {self.brand} {self.car_model} is at {self.current_speed} km/h'

car1 = Car('Toyota', 'Corolla', 30)
print(car1)