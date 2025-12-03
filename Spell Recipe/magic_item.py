from math import fabs


class MagicItem:

    def __init__(self, name: str, power: int):
        if not name:
            raise ValueError("Name cannot be empty")
        if power < 0:
            raise ValueError("Power must be >= 0")
        self._name = name
        self._power = power

    # TODO: Implement getter for name and power, and setter for power
    @property
    def power(self):
        return self._power
    
    @property
    def name(self):
        return self._name
    
    @power.setter
    def power(self, value:int):
        return self._power == value
    
    def upgrade(self, amount: int):
        # TODO: Implement upgrade logic to increase power
        self._power += amount

    def __eq__(self, other):
        # TODO: Implement equality comparison based on name and power
        if self._power == other._power and self._name == other._name:
            return True
        else:
            return False

    def __repr__(self):
        # TODO: Define __repr__ for MagicItem
        return f'{self._name}, {self._power}'
