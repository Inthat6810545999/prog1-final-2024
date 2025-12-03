# Name: Inthat # Student ID: 68010545999
class Dog:
    def speak(self):
        return 'Woof!'

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Boop Boop!"

while True:
    choice = input('Create (dog/cat/robot/exit): ')
    if choice.lower() == 'exit':
        print("Goodbye.")
        break
    elif choice.lower() == 'dog':
        choice = Dog()
        print(choice.speak())
    elif choice.lower() == 'cat':
        choice = Cat()
        print(choice.speak())
    elif choice.lower() == 'robot':
        choice = Robot()
        print(choice.speak())

