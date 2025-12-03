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

from typing import Type
import pytest
from exceptions import CraftException, BrokenItemException, InvalidProcessException
from item import Item
from resource import Resource
from tool import Tool
from recipe import Recipe
from crafter import Crafter

def test_1101_item_init_1():
    a = Item('Stick', 1, 2)
    assert a.name == 'Stick'
    assert a.mass == 1
    assert a.value == 2

def test_1102_item_init_2():
    a = Item('Stick', 1)
    assert a.name == 'Stick'
    assert a.mass == 1
    assert a.value == 0

def test_1103_item_init_3():
    a = Item('Stick')
    assert a.name == 'Stick'
    assert a.mass == 0
    assert a.value == 0

def test_1104_item_set():
    a = Item('Stick')
    a.value = 1
    assert a.value == 1

def test_1105_item_eq_t():
    a = Item('Stick', 1, 2)
    b = Item('Stick', 1, 2)
    assert a == b

def test_1106_item_eq_f():
    a = Item('Stick', 1, 2)
    c = Item('stick', 1, 2) # lower case
    d = Item('Stick', 2, 2) # wrong mass
    e = Item('Stick', 1, 3) # wrong value
    assert a != c
    assert a != d
    assert a != e

def test_1107_item_repr():
    a = Item('Stick', 1, 2)
    test_str = '[Stick, mass 1, $2]'
    assert str(a) == test_str

def test_1108_item_type_1():
    with pytest.raises(TypeError):
        a = Item('Stick', '1')

def test_1109_item_type_2():
    with pytest.raises(TypeError):
        a = Item('Stick', 1, '2')
    with pytest.raises(TypeError):
        a = Item('Stick', 1, None)

def test_1110_item_type_3():
    with pytest.raises(TypeError):
        a = Item()

def test_1111_item_value_1():
    with pytest.raises(ValueError):
        a = Item('')

def test_1111_item_value_2():
    with pytest.raises(ValueError):
        a = Item('Stick', -1) 
    with pytest.raises(ValueError):
        a = Item('Stick', 0, -1)