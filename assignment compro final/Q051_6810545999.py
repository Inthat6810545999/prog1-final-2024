# Name: Inthat # Student ID: 68010545999

class CoffeeMachine():
    def __init__(self, water, beans):
        self.__water_level = water 
        self.__beans_level = beans

    def __grind_beans(self):
        if self.__beans_level >= 10:
            self.__beans_level -= 10
        return "Grinding coffee beans..."


    def __heat_water(self):
        if self. __water_level >= 20:
            self.__water_level -= 20
        return "Heating water..."

    def __pour_espresso(self):
        return "Pouring espresso shot..."
    
    def make_espresso(self):
        if self.__water_level >= 20 and self.__beans_level >= 10:
            print(self.__heat_water())
            print(self.__grind_beans())
            print(self.__pour_espresso())
            print("Your espresso is ready!")
        else:
            print("Error: Please refill water or beans.")
    def get_status(self):
        return f"Water: {self.__water_level}, Beans: {self.__beans_level}"
    
start_water = int(input("Enter initial water level: "))
start_bean = int(input("Enter initial beans level: "))
machine = CoffeeMachine(start_water, start_bean)
while True:
    command = input('Enter command (make/status/exit): ')
    if command.lower() == 'exit':
        print('Goodbye.')
        break
    elif command.lower() == 'make':
        (machine.make_espresso())

    elif command.lower() == 'status':
        print(machine.get_status())




