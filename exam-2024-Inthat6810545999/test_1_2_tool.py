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

import pytest
from exceptions import CraftException, BrokenItemException, InvalidProcessException
from item import Item
from resource import Resource
from tool import Tool
from recipe import Recipe
from crafter import Crafter

def test_1201_tool_init_1():
    t1 = Tool('Chainsaw', 10, 500, ['saw', 'cut'], 90)
    assert t1.name == 'Chainsaw'
    assert t1.mass == 10
    assert t1.value == 500
    assert t1.functions == ['saw', 'cut']
    assert t1.durability == 90
    assert t1.experience == 0

def test_1202_tool_init_2():
    t1 = Tool('Chainsaw', 10, 500, ['saw', 'cut'])
    assert t1.name == 'Chainsaw'
    assert t1.mass == 10
    assert t1.value == 500
    assert t1.functions == ['saw', 'cut']
    assert t1.durability == 100
    assert t1.experience == 0

def test_1203_tool_init_3():
    t1 = Tool('Chainsaw', 10, 500)
    assert t1.name == 'Chainsaw'
    assert t1.mass == 10
    assert t1.value == 500
    assert t1.functions == []
    assert t1.durability == 100
    assert t1.experience == 0

def test_1204_tool_type_1():
    with pytest.raises(TypeError):
        # functions can't be tuple
        t1 = Tool('Chainsaw', 10, 500, ('saw', 'cut'))

def test_1205_tool_type_2():
    with pytest.raises(TypeError):
        # functions can't be plain string
        t1 = Tool('Chainsaw', 10, 500, 'saw')

def test_1206_tool_type_3():
    with pytest.raises(TypeError):
        t1 = Tool('Chainsaw', 10, 500, durability='1')

def test_1207_tool_value():
    with pytest.raises(ValueError):
        t1 = Tool('Chainsaw', 10, 500, durability=-1)

def test_1208_tool_use():
    t1 = Tool('Chainsaw')
    assert t1.durability == 100
    assert t1.experience == 0
    for i in range(1, 20):
        t1.use()
        assert t1.durability == 100 - i
        assert t1.experience == i

def test_1209_tool_broken():
    t1 = Tool('Chainsaw', durability = 0)
    with pytest.raises(BrokenItemException):
        t1.use()

def test_1210_tool_broken_complex():
    t1 = Tool('Chainsaw', durability = 100)
    with pytest.raises(BrokenItemException):
        for _ in range(105):
            t1.use()

def test_1211_tool_repair_simple():
    t1 = Tool('Chainsaw', 10, 500, durability=0)
    t1.repair()
    assert t1.durability == 100

def test_1212_tool_repair_complex():
    t1 = Tool('Chainsaw', 10, 500, durability=0)
    t1.repair(20)
    assert t1.durability == 20
    t1.repair()
    assert t1.durability == 100
    t1.repair(10)
    assert t1.durability == 110
    t1.repair()
    assert t1.durability == 110