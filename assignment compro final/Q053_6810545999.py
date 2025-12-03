# Name: Inthat # Student ID: 68010545999

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.speed = 0

    def accelarate(self, amount):
        if amount > 0:
            self.speed += amount
        print(f'{self.brand} accelerates.')
        
    def brake(self, amount):
        if amount > 0:
            self.speed -= amount
            if self.speed <= 0:
                self.speed = 0
        print(f'{self.brand} brakes.')
    
    def get_status(self):
        return f'Status: {self.brand} Speed: {self.speed}.'
    
    def __str__(self):
        return f'{self.brand}'
class Car(Vehicle):
    def __init__(self, brand, year, numdoors):
        super().__init__(brand, year)
        self.numdoors = numdoors
    
    def __str__(self):
        return super().__str__()

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def __str__(self):
        return super().__str__()
vehicles = []

while True:
    type = input("Register (car/motorcycle/done): ")
    if type.lower() == 'done':
        break
    elif type.lower() == 'motorcycle':
        brand = input("Enter brand: ")
        year = input("Enter year: ")
        side = input("Has sidecar (True/False): ")
        if side.lower() == 'true':
            side = 'True'
        elif side.lower() == 'false':
            side = 'False'
        motor = Motorcycle(brand, year, side)
        vehicles.append(motor)
        print('Vehicle added.')
    elif type.lower() == 'car':
        brand = input("Enter brand: ")
        year = input("Enter year: ")
        num_door = input('Enter number of doors: ')
        car = Car(brand, year, num_door)
        vehicles.append(car)
        print('Vehicle added.')
    else:
        print("Invalid input.")
        
print('--- Registered Vehicles ---')
for vehicle in vehicles:
    print(vehicle)
print("---------------------------")
while True:
    parts = input("Enter command: ").split()
    if len(parts) == 1 and parts[0].lower() == 'exit':
            print('Goodbye.')
            break
    elif len(parts) == 1 and parts[0].lower() == 'status':
        for vehicle in vehicles:
            print(vehicle.get_status())
        
    elif len(parts) !=  3:
        print('Invalid command.')

    else:
        command, name, acc = parts[0], parts[1], int(parts[2])
        vehicle_found = None
        for vehicle in vehicles:
            if name not in vehicle.brand:
                vehicle_found = vehicle
                break
        if vehicle_found == None:
            print("Vehicle not found.")
            continue
        if command.lower() == 'accel':
            for vehicle in vehicles:
                if vehicle.brand.lower() == name.lower():
                    vehicle.accelarate(acc)

        elif command.lower() == 'break':
            for vehicle in vehicles:
                if vehicle.brand.lower() == name.lower():
                    vehicle.brake(acc)
        

            