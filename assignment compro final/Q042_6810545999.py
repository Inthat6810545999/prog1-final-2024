# Name: Inthat # Student ID: 68010545999
class Motorcycle():
    def __init__(self):
        self.speed = 0
        self.mileage = 0
    
    def starting(self):
        return f'"Motorcycle is starting...'
    def accelerate(self, amount):
        self.speed += amount
        return f'"Accelerating... Current speed: {self.speed} km/h".'
    def add_mileage(self, distance):
        self.mileage += distance
        return None
    def stop(self):
        self.speed = 0
        return f'Motorcycle has stopped.'
    def status(self):
        return f'"Current Speed: {self.speed} km/h, Total Mileage: {self.mileage} km".'
    
bike = Motorcycle()
while True:
    com = input("Enter command: ")
    if com.lower() == 'exit':
        print("Goodbye.")
        break

    elif com.lower() == 'start':
        print(bike.starting())

    elif 'accel' in com.lower():
        try:
            parts = com.split()
            value = int(parts[-1])
            print(bike.accelerate(value))
        except:
            print("Invalid command. Please try again.")
    elif 'mileage' in com.lower():
        try:
            p = com.split()
            v = int(p[-1])
            (bike.add_mileage(v))
        except:
            print("Invalid command. Please try again.")

    elif com.lower() == 'status':
        print(bike.status())

    elif com.lower() == 'stop':
        print(bike.stop())
    else:
        print("Invalid command. Please try again.")