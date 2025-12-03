"""
This module defines basic behavior of tools, extended from items.

Part of the 01219114/5 Examination at Kasetsart University
See README.md for details

Import whatever you need, but here should be enough.
WORK ON item.py FIRST!
"""

from re import S
from types import NoneType
#from typing import Type, Tuple, Dict, List # import more if you need them
from exceptions import BrokenItemException
from item import Item

class Tool(Item):
    """
    LEVEL 1: A Tool is a simple object of its own.
    LEVEL 2: A Tool is based on an Item. (Extends Item class.)

    LEVEL 1: Required attributes of a tool IN ADDITION TO Item:
    - functions: list of str (optional, default empty list) <<GET>>
    - durability: int (optional, >= 0, default 100) <<GET>>
    - experience: int (do not include in init, set to 0) <<GET>>

    LEVEL 1: A Tool must have the following PUBLIC methods.
    + use(self) -> None
    + repair(self, by: int) -> None

    More information is provided in the method header.
    """

    def __init__(self, name, mass, value, functions:list = [], durability:int = 100) -> None:
        """
        >>> t1 = Tool('Chainsaw', 10, 500, ['saw', 'cut'])
        >>> t1.functions
        ['saw', 'cut']
        """
        super().__init__(name, mass, value)
        # TODO continue
        self.__functions = functions
        self.__durability = durability
        self.__experience = 0
    


    def use(self) -> None:
        """
        Check durability. If zero, raise BrokenItemException as defined above.
        Reduce durability by 1.
        Increase experience by 1.        

        >>> t1 = Tool('Chainsaw', 10, 500, functions=['saw', 'cut'])
        >>> t1.durability, t1.experience
        (100, 0)
        >>> t1.use()
        >>> t1.use()
        >>> t1.durability, t1.experience
        (98, 2)
        """
        if self.__durability <= 0:
            raise ValueError(BrokenItemException)
        elif self.__durability > 0:
            self.__durability -= 1
            self.__experience += 1
    
    @property
    def functions(self):
        return list(self.__functions)
    @property
    def durability(self) -> int:
        return self.__durability

    @property
    def experience(self) -> int:
            return self.__experience

    def repair(self, by: int = 0) -> None:
        """
        Increase durability based on the value "by". If "by" is not given, then
        just set the durability to 100 if it's lower than 100.

        Obviously, "by" cannot be negative.

        Durability must increase by the amount specified in "by" param.

        >>> t4 = Tool('Pencil', 0, 1, durability = 200)
        >>> t4.repair(by = 20)
        >>> t4.durability
        220

        Durability must remain the same if 100 or above and "by" is not given.

        >>> t4 = Tool('Pencil', 0, 1, durability = 200)
        >>> t4.repair()
        >>> t4.durability
        200

        Or repair up to 100 if already under 100.
        
        >>> t4 = Tool('Old Pencil', 0, 1, durability = 10)
        >>> t4.repair()
        >>> t4.durability
        100

        """


        if by == 0 and self.__durability < 100:
            self.__durability = 100
        elif by == 0 and self.durability >= 100:
            self.__durability += 0
        else:
            self.__durability += by
        
    # TODO implement properties

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
