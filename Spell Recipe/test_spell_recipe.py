import pytest
from spell import Spell
from spell_recipe import SpellRecipe

def test_spell_recipe_creation():
    fire = Spell('Fire', 10)
    wind = Spell('Wind', 5)
    recipe = SpellRecipe('Fire Burst', [fire, wind], [fire])

    assert recipe.name == 'Fire Burst'
    assert len(recipe.ingredients) == 2
    assert len(recipe.results) == 1
    assert recipe.ingredients[0].name == 'Fire'
    assert recipe.results[0].name == 'Fire'
