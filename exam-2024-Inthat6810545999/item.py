"""
This module defines basic behavior of items in the problem.

Part of the 01219114/5 Examination at Kasetsart University
See README.md for details

Import whatever you need, but here should be enough.
WORK ON THIS FILE FIRST!
"""

class Item:
    """
    LEVEL 1: Designates an item. All items have the following attributes:

    # name: str (required, cannot be empty string) <<GET>>
    # mass: int (optional, >= 0, default 0) <<GET>>
    # value: int (optional, >= 0, default 0) <<GET, SET>>
    
    ^ LEVEL 2:
    ^ This means public or protected or private??? Implement accurately!

    LEVEL 2: Using properties with appropriate @property-based getters and
    setters will net a higher score. Do not use method-based getters and
    setters.
    """

    def __init__(self, name, mass, value) -> None:
        """
        LEVEL 1: This defines an item named Stick, having mass 1 and value 2.

        >>> a = Item('Stick', 1, 2)
        >>> a.name
        'Stick'
        >>> a.mass
        1
        >>> a.value
        2

        The value must have a setter, meaning that its value can be changed.
        >>> a.value = 4
        >>> a.value
        4
        """
        self.name = name
        self.mass = mass
        self.value = value

    #TODO implement properties, or not, up to you

    def __eq__(self, other) -> bool:
        """
        LEVEL 1: Items are considered equal when the names, masses, and values
        match EXACTLY.

        >>> a = Item('Stick', 1, 2)
        >>> b = Item('Stick', 1, 2)
        >>> c = Item('stick', 1, 2) # lower case
        >>> d = Item('Stick', 2, 2) # wrong mass
        >>> e = Item('Stick', 1, 3) # wrong value

        >>> a == b
        True
        >>> a == c
        False
        >>> a == d
        False
        >>> a == e
        False
        """
        if self.name == other.name and self.mass == other.mass and self.value == other.value:
            return True
        else:
            return False

    def __repr__(self) -> str:
        """
        LEVEL 1: In addition to initialization, they must produce lines like
        this when printed:

        >>> a = Item('Stick', 1, 2)
        >>> print(a)
        [Stick, mass 1, $2]

        >>> print(Item('Cheese Wheel', 10, 60))
        [Cheese Wheel, mass 10, $60]

        Brackets are mandatory.
        """
        return (f'[{self.name}, mass {self.mass}, ${self.value}]')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
