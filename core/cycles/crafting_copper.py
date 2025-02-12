import time

def crafting_copper(engine):
    engine.logger.info("Gathering")
    
    result = engine.safe_api_call(engine.api.gathering, "Gathering failed")
    if result is None:
        return

    engine.logger.info("Gathering complete")
    engine.cooldown(result) 

    character_data = result.get("character", {})
    inventory_max, total_items, inventory = engine.get_inventory_status(character_data)
    engine.logger.info(f"Inventory: {total_items}/{inventory_max}")
    
    if total_items < inventory_max - 1:
        return

    engine.logger.info("Inventory is full. Proceeding to move and craft copper.")
    if not engine.move(1, 5, "Error moving to (1,5)"):
        return

    copper_ore_quantity = engine.get_copper_ore_quantity(inventory)
    craft_amount = copper_ore_quantity // 8
    if craft_amount > 0:
        engine.logger.info(f"Crafting {craft_amount} copper (from {copper_ore_quantity} copper ore)...")
        if not engine.craft("copper", craft_amount, "Error crafting copper"):
            return
    else:
        engine.logger.info("Not enough copper ore to craft copper (need at least 8).")

    if not engine.move(2, 0, "Error moving to (2,0)"):
        return
