import time
import logging
from core.api import ArtifactAPI
from core.cycles.crafting_copper import crafting_copper
from core.cycles.fight import fight

class GameEngine:
    def __init__(self, character: str):
        self.character = character
        self.api = ArtifactAPI(self, character)
        self.logger = logging.getLogger(self.character)
    
    def cooldown(self, response: dict, default: int = 5) -> None:
        cd = response.get("cooldown", {}).get("total_seconds", default)
        time.sleep(cd)

    def safe_api_call(self, func, error_message: str, *args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            self.logger.error(f"{error_message}. Retrying in 10 seconds...")
            time.sleep(10)
        return result

    def move(self, x: int, y: int, error_message: str) -> bool:
        result = self.safe_api_call(self.api.move, error_message, x, y)
        if result is None:
            return False
        cooldown(result)
        return True

    def craft(self, code: str, quantity: int, error_message: str) -> bool:
        result = self.safe_api_call(self.api.crafting, error_message, code, quantity)
        if result is None:
            return False
        cooldown(result)
        return True

    def get_inventory_status(self, character_data: dict):
        inventory_max = character_data.get("inventory_max_items", 0)
        inventory = character_data.get("inventory", [])
        total_items = sum(item.get("quantity", 0) for item in inventory)
        return inventory_max, total_items, inventory

    def get_copper_ore_quantity(self, inventory: list) -> int:
        return sum(item.get("quantity", 0) for item in inventory if item.get("code") == "copper_ore")
    
    def perform_fight_cycle(self):
        fight(self)

    def perform_crafting_copper(self):
        crafting_copper(self)