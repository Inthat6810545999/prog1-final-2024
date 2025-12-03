"""
This module defines basic behavior of resources, extended from items.

Part of the 01219114/5 Examination at Kasetsart University
See README.md for details

Import whatever you need, but here should be enough.
WORK ON item.py FIRST!
"""

import copy
from typing import Type, Tuple, Dict, List # import more if you need them
from exceptions import InvalidProcessException
from item import Item

class Resource(Item):
    """
    This is quite hard. Please don't attempt if you are unsure.

    LEVEL 3: A Resource is an Item that can be processed by a Tool.
    
    You must define the following attribute in addition to what's in Item:
    
    - valid_processes: Dict[str, Tuple[Type['Item'], int]] (optional, default
      empty dict) <<GET>>. This attribute encodes what happens when the item
      is processed by a tool and results in one or more items of the same type.
      See doctest for example.

    You must define the following public method:

    + process(self, functions: str) -> List[Item]

    See below.

    """
    def __init__(self, name: str, mass: int, value: int,
                 valid_processes: Dict[str, Tuple[Type['Item'], int]]) -> None:
        """
        In this case, an item named Log can be processed into 10 instances
        of Stick using the process 'saw'.

        >>> b = Resource('Log', 10, 20, {'saw': (Item('Stick', 1, 2), 10)})
        >>> b.valid_processes['saw'][0].name
        'Stick'
        >>> b.valid_processes['saw'][1]
        10
        
        The following defines a Stick that accepts two processes, 'cut' and
        'light'. The 'cut' process produces four instances of Item called
        'Chopsticks (Pair)'. The 'light' process produces one instance of
        Item called 'Burning Stick'.
        >>> c = Resource('Stick', 1, 2, \
                     {'cut': (Item('Chopsticks (Pair)', 0, 2), 4), \
                      'light': (Item('Burning Stick', 0, 2), 1)})
        >>> sorted(c.valid_processes.keys())
        ['cut', 'light']
        """
        self.name = name 
        self.mass = mass 
        self.value = value
        self.vaid_processes = valid_processes

    # TODO implement properties

    def process(self, functions: str) -> List[Item]:
        """
        LEVEL 3: When the Item is being processed by a Tool (see below), the
        tool will send the list of functions to this Item. You must find the
        first function with a matching process in self.valid_processes, then
        process based on that match.

        For example, a shovel can be used to dig, bury, and bash. In that case,
        you should try digging first. If there's nothing that can be done with
        digging, then you should bury, and then finally bash. If nothing works,
        raise InvalidProcessException without message.

        MUST return a list of multiple items. Warning that each item MUST be
        distinct from each other, so be careful and use `copy` when needed!

        Suppose we have a 'Stick' Item that accepts 'cut' and 'light' functions
        >>> c = Resource('Stick', 1, 2, \
                     {'cut': (Item('Chopsticks (Pair)', 0, 1), 4), \
                      'light': (Item('Burning Stick', 1, 1), 1)})

        Then we want to process it with a tool that can 'cut' and 'saw'.        
        >>> processed = c.process(['cut', 'saw'])

        MUST produce four 'Chopsticks (Pair)', one looking like this:
        >>> print(processed[0])
        [Chopsticks (Pair), mass 0, $1]

        MUST produce 4 of them (since the dict of processes state 4 copies):
        >>> len(processed)
        4

        And they MUST be distinct:
        >>> processed[0] is processed[1]
        False

        Alternatively, if we want to process it with a tool that can 'light':
        >>> processed = c.process(['light'])
        >>> print(processed[0])
        [Burning Stick, mass 1, $1]

        Another kind of product is made instead.
        """
        pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
