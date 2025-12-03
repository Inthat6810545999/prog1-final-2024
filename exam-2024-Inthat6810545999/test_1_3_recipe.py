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

def test_1301_recipe_init():
    item1 = Item('10 baht coin', 0, 10)
    item2 = Item('20 baht note', 0, 20)
    recipe = Recipe('Split Bank', [copy.copy(item2)], 2*[copy.copy(item1)])

def test_1302_recipe_repr():
    item1 = Item('10 baht coin', 0, 10)
    item2 = Item('20 baht note', 0, 20)
    recipe = Recipe('Split Bank', [copy.copy(item2)], 2*[copy.copy(item1)])
    assert (str(recipe) == "RECIPE: Split Bank\nINPUT:\n- 20 baht note\nOUTPUT:\n- 10 baht coin\n- 10 baht coin\nEND RECIPE")

def test_1303_recipe_type_1():
    item1 = Item('10 baht coin', 0, 10)
    item2 = Item('20 baht note', 0, 20)
    with pytest.raises(TypeError):
        recipe = Recipe('Split Bank', copy.copy(item2), 2*[copy.copy(item1)])

def test_1304_recipe_type_2():
    item1 = Item('10 baht coin', 0, 10)
    item2 = Item('20 baht note', 0, 20)
    with pytest.raises(TypeError):
        recipe = Recipe('Split Bank', [copy.copy(item2)], copy.copy(item1))

def test_1305_recipe_value_1():
    item2 = Item('20 baht note', 0, 20)
    with pytest.raises(ValueError):
        recipe = Recipe('Split Bank', [], [item2])

def test_1306_recipe_value_2():
    item1 = Item('10 baht coin', 0, 10)
    with pytest.raises(ValueError):
        recipe = Recipe('Split Bank', [item1], [])

def test_1307_recipe_value_3():
    item1 = Item('10 baht coin', 0, 10)
    with pytest.raises(ValueError):
        recipe = Recipe('Split Bank', [item1], [item1])

def test_1308_recipe_value_4():
    item1 = Item('10 baht coin', 0, 10)
    item2 = Item('20 baht note', 0, 20)
    with pytest.raises(ValueError):
        recipe = Recipe('', [copy.copy(item2)], 2*[copy.copy(item1)])