# Part of the 01219114/5 Examination at Kasetsart University
# See README.md for details

# DO NOT MODIFY THIS FILE

class InvalidProcessException(Exception):
    """
    Signals that an item cannot be processed as the tool's provided functions
    do not have any match with the item's permitted processes.
    Do not modify this class.
    """
    pass

class BrokenItemException(Exception):
    """
    Signals that an item is broken and cannot be used.
    Do not modify this class.
    """
    pass

class CraftException(Exception):
    """
    Signals that crafting process has failed.
    Do not modify this class.
    """
    pass