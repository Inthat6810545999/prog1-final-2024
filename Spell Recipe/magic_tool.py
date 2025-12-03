from magic_item import MagicItem
class MagicTool:

    def __init__(self, name: str, base_damage: int, durability: int = 100) -> None:
        self._name = name
        self._base_damage = base_damage
        self._durability = durability
        self._experience = 0
        self._gem = None  # Start with no gem

    # TODO: Implement socket method to insert a gem
    def socket(self, gem: MagicItem) -> None:
        if self._gem is not None:
            print(f"{self._name} already has a gem socketed.")
            return
        self._gem = gem
        print(f"Socketed {gem.name} into {self._name}.")

    # TODO: Implement unsocket method to remove and return the gem
    def unsocket(self):
        pass

    # TODO: Implement total_damage method
    def total_damage(self):
        pass

    # TODO: Implement use method that handles durability and returns total damage
    def use(self):
        pass
