import pytest
from magic_item import MagicItem
from magic_tool import MagicTool
from spell import Spell
from spell_recipe import SpellRecipe
from inventory import Inventory


# --- TEST 1: Test MagicItem ---
def test_magic_item_creation():
    item = MagicItem("Ruby", 50)
    assert item.name == "Ruby"
    assert item.power == 50

def test_magic_item_upgrade():
    item = MagicItem("Ruby", 50)
    item.upgrade(10)
    assert item.power == 60
    with pytest.raises(ValueError):
        item.upgrade(-1)

def test_magic_item_eq():
    item1 = MagicItem("Ruby", 50)
    item2 = MagicItem("Ruby", 50)
    item3 = MagicItem("Emerald", 40)
    assert item1 == item2
    assert item1 != item3

# --- TEST 2: Test Spell ---
def test_spell_creation():
    spell = Spell("Fireball", 100)
    assert spell.name == "Fireball"
    assert spell.power == 100

def test_spell_upgrade():
    spell = Spell("Fireball", 100)
    spell.upgrade(50)
    assert spell.power == 150

def test_spell_eq():
    spell1 = Spell("Fireball", 100)
    spell2 = Spell("Fireball", 100)
    spell3 = Spell("Iceball", 90)
    assert spell1 == spell2
    assert spell1 != spell3

# --- TEST 3: Test SpellRecipe ---
def test_spell_recipe_creation():
    fire = Spell("Fire", 50)
    wind = Spell("Wind", 30)
    recipe = SpellRecipe("Fire Wind", [fire, wind], [fire])

    assert recipe.name == "Fire Wind"
    assert len(recipe.ingredients) == 2
    assert recipe.ingredients[0].name == "Fire"
    assert recipe.ingredients[1].name == "Wind"
    assert recipe.results[0].name == "Fire"

def test_spell_recipe_property():
    fire = Spell("Fire", 50)
    wind = Spell("Wind", 30)
    recipe = SpellRecipe("Fire Wind", [fire, wind], [fire])

    # Test properties
    assert recipe.name == "Fire Wind"
    assert len(recipe.ingredients) == 2
    assert recipe.results[0].name == "Fire"

# --- TEST 4: Test MagicTool ---
def test_magic_tool_creation():
    tool = MagicTool("Magic Wand", base_damage=20, durability=100)
    assert tool.name == "Magic Wand"
    assert tool.base_damage == 20
    assert tool.durability == 100

def test_magic_tool_socket():
    tool = MagicTool("Magic Wand", base_damage=20)
    gem = MagicItem("Ruby", 50)
    tool.socket(gem)
    assert tool.gem == gem
    assert tool.total_damage() == 25  # 20 + (50 // 10)

def test_magic_tool_unsocket():
    tool = MagicTool("Magic Wand", base_damage=20)
    gem = MagicItem("Ruby", 50)
    tool.socket(gem)
    unsocketed_gem = tool.unsocket()
    assert unsocketed_gem == gem
    assert tool.gem is None

def test_magic_tool_use():
    tool = MagicTool("Magic Wand", base_damage=20, durability=2)
    damage = tool.use()
    assert damage == 25  # 20 + (50 // 10)
    assert tool.durability == 1
    assert tool.experience == 1

    tool.use()
    assert tool.durability == 0
    assert tool.experience == 2

    with pytest.raises(BrokenItemException):
        tool.use()

# --- TEST 5: Test Inventory ---
def test_inventory_add_and_count():
    inventory = Inventory()
    item = MagicItem("Ruby", 50)
    tool = MagicTool("Magic Wand", base_damage=20)
    
    inventory.add(item)
    inventory.add(tool)
    inventory.add(item)

    assert inventory.count(item) == 2
    assert inventory.count(tool) == 1

def test_inventory_remove():
    inventory = Inventory()
    item = MagicItem("Ruby", 50)
    inventory.add(item)
    inventory.remove(item)
    assert inventory.count(item) == 0

    with pytest.raises(ValueError):
        inventory.remove(item)

def test_inventory_find_by_type():
    inventory = Inventory()
    item = MagicItem("Ruby", 50)
    tool = MagicTool("Magic Wand", base_damage=20)

    inventory.add(item)
    inventory.add(tool)

    tools = inventory.find_by_type("MagicTool")
    assert len(tools) == 1
    assert tools[0].name == "Magic Wand"
