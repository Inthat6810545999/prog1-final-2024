# Name: Inthat # Student ID: 68010545999

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year 
        

class Car(Vehicle):
    def __init__(self, brand, year, numdoors):
        super().__init__(brand, year)
        self.numdoors = numdoors

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

type = input("Register (car/motorcycle): ")
brand = input("Enter brand: ")
year = input("Enter year: ")
if type.lower() == 'motorcycle':
    side = input("Has sidecar (True/False): ")
    motor = Motorcycle(brand, year, side)
    print(f'Registered: Brand: {motor.brand}, Year: {motor.year}, Sidecar: {motor.has_sidecar}')
elif type.lower() == 'car':
    num_door = input('Enter number of doors: ')
    car = Car(brand, year, num_door)
    print(f'Registered: Brand: {car.brand}, Year: {car.year}, Door: {car.numdoors}')