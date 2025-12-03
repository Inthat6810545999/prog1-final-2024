from os import name
from typing import Self
from matplotlib.mathtext import RasterParse
from numpy import power


class Spell:
    """
    LEVEL 1:
    A Spell has:
    # name: str (required, cannot be empty) <<GET>>
    # power: int (required, >= 0) <<GET, SET>>

    LEVEL 2:
    Use @property getters + setter for power.
    Validate all inputs.

    LEVEL 3:
    Implement __eq__ to compare Spells by name + power.
    """

    def __init__(self, name: str, power: int) -> None:
        if not name:
            raise ValueError("Name cannot be empty.")
        if power < 0:
            raise ValueError("Power must be >= 0")
        self._name = name
        self._power = power

    # TODO: Implement getter and setter for name and power
    @property
    def name(self):
        return self._name
    
    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, value:int):
        if value < 0:
            raise ValueError
        self._power = value

    def upgrade(self, amount: int):
        # TODO: Upgrade power by amount, if amount < 0 raise ValueError
        if amount < 0:
            raise ValueError
        else:
            self._power += amount

    def __eq__(self, other):
        # TODO: Compare Spells by name and power

        if self._name == other._name and self._power == other._power:
            return True
        else:
            return False

    def __repr__(self):
        # TODO: Define a repr for Spell objects
        return f'{self._name}, {self._power}'
