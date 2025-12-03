"""
This module defines basic behavior of resources, extended from items.

Part of the 01219114/5 Examination at Kasetsart University
See README.md for details

Import whatever you need, but here should be enough.
WORK ON item.py FIRST!
"""

import copy
#from typing import Type, Tuple, Dict, List # import more if you need them
from item import Item
from recipe import Recipe
from exceptions import CraftException

class Crafter:
    """
    LEVEL 1: Just define a crafter. It has following attributes:

    # name: str (required, cannot be empty string) <<GET>>
    # inventory: List[Item] (initialize as empty list) <<GET>>
    
    ^ LEVEL 2:
    ^ This means public or protected or private??? Implement accurately!

    It also has additional public methods:

    + craft(self, recipe: Recipe, ingredients: List[Item]) -> List[Item]
    + add_item(self, item: Item) -> None
    """

    def __init__(self, name: str) -> None:
        """
        >>> c = Crafter('My Crafter')
        >>> print(c.name)
        My Crafter
        """
        pass

    # TODO implement properties

    def __str__(self):
        """
        >>> c = Crafter('My Crafter')
        >>> print(c)
        [Crafter: 'My Crafter' (0 items)]
        """
        pass

    def add_item(self, item: Item) -> None:
        """
        Level 1: Add item to self.inventory.

        Item add order must be preserved. Ignore any sorting.
        >>> c = Crafter('My Crafter')
        >>> c.add_item(Item('Wallet', 1, 200))
        >>> print(c.inventory)
        [[Wallet, mass 1, $200]]
        >>> c.add_item(Item('AAAAAA', 1, 0))
        >>> print(c.inventory)
        [[Wallet, mass 1, $200], [AAAAAA, mass 1, $0]]
        """
        pass

    def craft(self, recipe: Recipe) -> None:
        """
        LEVEL 3:
        The method reads contents of `recipe` and checks if the Item objects
        contained in `self.inventory` are enough to meet the `recipe`. If so,
        convert only those items into results. Add the results back into the
        inventory.

        If there is enough ingredient for multiple actions, perform only once.

        Always use Item objects with lower index (earlier in the inventory)
        first.

        If crafting fails, raise CraftException.

        This method does require a bit of algorithm. If you are uncomfortable
        with it, leave it for later. You can follow the algorithm I provide in
        comments below or use your own.

        >>> c = Crafter('My Crafter')
        >>> input_items = 2*[Item('Stick', 0, 0)]
        >>> output_items = [Item('Chopsticks (pair)', 0, 1)]
        >>> r = Recipe('Pair Sticks', input_items, output_items)
        >>> c.add_item(Item('Stick', 0, 0))
        >>> c.add_item(Item('Stick', 0, 0))
        >>> c.craft(r)
        >>> print(c.inventory[0])
        [Chopsticks (pair), mass 0, $1]
        """
        # Hey isekaijin. This is Igor, your resident dwarf hacker.
        # This part is a bit tough so here's a simple algorithm that works.
        # Not the best, but works!

        # (1-3) check that crafting is possible
        ## 1. make deep copy of recipe input

        ## 2. make deep copy of inventory

        ## 3. search each item to confirm that it can be crafted, popping from
        ## the copy of inventory to ensure it cannot be used twice and to
        ## simulate actual item consumption. During this process, if we cannot
        ## find any input item in the inventory, we can raise CraftException
        ## immediately.


        # (4-5) beyond this point means crafting can proceed, so let's craft
        # for real (i.e. commit the results)
        ## 4. overwrite main inventory with the copy

        ## 5. add the crafted items to the inventory

        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
