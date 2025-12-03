"""
This module defines recipes for the crafting problem.

Part of the 01219114/5 Examination at Kasetsart University
See README.md for details

Import whatever you need, but here should be enough.
WORK ON item.py FIRST!
"""

import copy
from tkinter.font import names
from typing import List # import more if you need them
from item import Item

class Recipe:
    """
    LEVEL 1: 

    A recipe consists of attributes:

    # name: str (must not be empty string) <<GET>>
    # input: List[Item] (must not be empty list) <<GET>>
    # output: List[Item] (must not be empty list, must not be same as input)
        <<GET>>

    It has no methods other than __init__ and __str__.

    For the problem, __str__ is already provided. No need to fix, except ...
    maybe if it needs a bit ... linting?
    """
    def __init__(self, name: str,
                 input_items: List[Item], output_items: List[Item]) -> None:
        """
        LEVEL 1: Initializes the object.

        >>> item1 = Item('10 baht coin', 0, 10)
        >>> item2 = Item('20 baht note', 0, 20)
        >>> recipe = Recipe('Split Bank', [copy.copy(item2)], 2*[copy.copy(item1)])
        """
        self.name = name
        self._input = input_items
        self._output = output_items

    def __str__(self) -> str:
        """
        LEVEL 0: Outputs the string representation of the object.

        This is a freebie task. You might want to check with pylint for proper
        PEP8 compliance, but other than that there is no logic to change.

        >>> item1 = Item('10 baht coin', 0, 10)
        >>> item2 = Item('20 baht note', 0, 20)
        >>> recipe = Recipe('Split Bank', [copy.copy(item2)], 2*[copy.copy(item1)])
        >>> print(recipe)
        RECIPE: Split Bank
        INPUT:
        - 20 baht note
        OUTPUT:
        - 10 baht coin
        - 10 baht coin
        END RECIPE
        """

        result = f'RECIPE: {self.name}\nINPUT:\n'
        for i in self._input:
            result += f'- {i.name}\n'
        result += 'OUTPUT:\n'
        for i in self._output:
            result += f'- {i.name}\n'
        result += 'END RECIPE'
        return result

    # TODO implement properties
    




if __name__ == '__main__':
    import doctest
    doctest.testmod()
