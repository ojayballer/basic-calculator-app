class Vehicle():
    def __init__(self):
     def move(self):
        print("vehicle is moving")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        
    def move(self):
        print("car is moving")
class electricCar(Car):
     def __init__(self):
         super().__init__()
     def move(self):
         print("electricCar is moving")
car=Car()
car.move()