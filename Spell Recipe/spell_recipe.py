from spell import Spell
class SpellRecipe:
    """
    LEVEL 1:
    Attributes:
    - name: str (non-empty) <<GET>>
    - ingredients: List[Spell] (non-empty) <<GET>>
    - results: List[Spell] (non-empty, not the same as ingredients) <<GET>>

    LEVEL 2:
    Implement property-based getters.
    Return copies of ingredients and results to avoid aliasing.
    """

    def __init__(self, name: str, ingredients: list[Spell], results: list[Spell]) -> None:
        self._name = name
        self._ingredients = ingredients
        self._results = results

    # TODO: Implement properties for name, ingredients, and results
    # name: Get only
    @property
    def name(self):
        return self._name
    @property
    def ingredients(self):
        return self._ingredients
    @property
    def results(self):
        return self._results

    # ingredients: Get only (return a copy)
    # results: Get only (return a copy)
