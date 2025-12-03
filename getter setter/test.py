from hmac import new
#get set

class car:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
    @property
    def value(self):
        return self.__value
    @property
    def name(self):
        return self.__name
    
    @value.setter
    def value(self, newvalue):
        self.__value = newvalue
    

toyota = car("Son", 1)
print(toyota.name)
toyota.value = 2
print(toyota.value)

