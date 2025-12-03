"""
This is the basic test module for the 2024 examination to be used with pytest.

Part of the 01219114/5 Examination at Kasetsart University
See README.md for details

THIS IS A TEST FILE. DO NOT MODIFY THIS FILE. NOT EVEN FOR PYLINT COMPLIANCE.
(PYLINT SCORE FOR THIS FILE IS NOT USED!)
MALICIOUS MODIFICATION (TO INFLATE POINTS) WILL RESULT IN ACADEMIC DISHONESTY
REVIEW AND POSSIBLE SUSPENSION OR EXPULSION.

thing being tested.
You earn 1 point per test.
GLHF!
"""

import copy
import pytest
from exceptions import CraftException, BrokenItemException, InvalidProcessException
from item import Item
from resource import Resource
from tool import Tool
from recipe import Recipe
from crafter import Crafter

def test_1401_crafter_init_1():
    c = Crafter('My Crafter')
    assert c.name == 'My Crafter'

def test_1402_crafter_init_2():
    c = Crafter('Not My Crafter')
    assert c.name == 'Not My Crafter'

def test_1403_crafter_init_3():
    c = Crafter('My Crafter Again')
    assert c.inventory == []

def test_1404_crafter_repr():
    c = Crafter('My Crafter')
    assert str(c) == '[Crafter: \'My Crafter\' (0 items)]'

def test_1405_crafter_add_1():
    c = Crafter('My Crafter')
    c.add_item(Item('Stick', 1, 2))
    assert c.inventory[-1].name == 'Stick'

def test_1406_crafter_add_2():
    c = Crafter('My Crafter')
    c.add_item(Item('Stick', 1, 2))
    assert c.inventory[-1].name == 'Stick'
    c.add_item(Item('Block', 1, 2))
    assert c.inventory[-1].name == 'Block'

def test_1407_crafter_type():
    with pytest.raises(TypeError):
        c = Crafter()

def test_1408_crafter_value():
    with pytest.raises(ValueError):
        c = Crafter('')