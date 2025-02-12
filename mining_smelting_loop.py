import time
import json
from api import ArtifactAPI

if __name__ == "__main__":
    character = "MrSpeak"
    api = ArtifactAPI(character)
    
    while True:
        result = api.gathering()
        if result is None:
            print("Error performing gathering. Retrying in 10 seconds...")
            time.sleep(10)
            continue

        print(json.dumps(result, indent=2))
        
        cooldown_data = result.get("cooldown", {})
        cooldown_seconds = cooldown_data.get("total_seconds", 5)  # default to 5 seconds if missing
        time.sleep(cooldown_seconds)
        
        character_data = result.get("character", {})
        inventory_max = character_data.get("inventory_max_items", 0)
        inventory = character_data.get("inventory", [])

        total_items = sum(item.get("quantity", 0) for item in inventory)
        print(f"Inventory: {total_items}/{inventory_max}")
        
        # If inventory is not full, wait the cooldown and gather again
        # The -1 is a hack to avoid the case where the inventory is full but the character is still gathering
        if total_items < inventory_max - 1 :
            print("Inventory not full. Continuing to gather.")
            continue
        else:
            print("Inventory is full. Proceeding to move and craft copper.")
            move_result = api.move(1, 5)
            if move_result is None:
                print("Error moving character to (1,5). Retrying in 10 seconds...")
                time.sleep(10)
                continue

            cooldown_data = move_result.get("cooldown", {})
            cooldown_seconds = cooldown_data.get("total_seconds", 5)
            time.sleep(cooldown_seconds)
            # Calculate how many copper ore you have
            copper_ore_quantity = sum(
                item.get("quantity", 0) for item in inventory if item.get("code") == "copper_ore"
            )
            # Determine how many copper items to craft (each copper is made from 8 copper ore)
            craft_amount = copper_ore_quantity // 8

            if craft_amount > 0:
                print(f"Crafting {craft_amount} copper (from {copper_ore_quantity} copper ore)...")
                crafting_result = api.crafting("copper", craft_amount)
                if crafting_result is None:
                    print("Error crafting copper. Retrying in 10 seconds...")
                    time.sleep(10)
                    continue
                # Wait for the crafting cooldown
                crafting_cooldown = crafting_result.get("cooldown", {}).get("total_seconds", 5)
                print(f"Crafting completed. Cooldown: {crafting_cooldown} seconds.")
                time.sleep(crafting_cooldown)
            else:
                print("Not enough copper ore to craft copper (need at least 8 copper ore).")
                # Wait the gathering cooldown before trying again
                time.sleep(cooldown_seconds)
            
            move_result = api.move(2, 0)
            if move_result is None:
                print("Error moving character to (2, 0). Retrying in 10 seconds...")
                time.sleep(10)
                continue

            cooldown_data = move_result.get("cooldown", {})
            cooldown_seconds = cooldown_data.get("total_seconds", 5)
            time.sleep(cooldown_seconds)
            
