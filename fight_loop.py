import time
from api import ArtifactAPI

if __name__ == "__main__":
    character = "MrSpeak"
    api = ArtifactAPI(character)
    
    while True:
        result = api.fight()
        if result is None:
            print("Error performing fight. Retrying in 10 seconds...")
            time.sleep(10)
            continue

        # Extract the cooldown
        cooldown_data = result.get("cooldown", {})
        cooldown_seconds = cooldown_data.get("total_seconds", 5)  # default to 5 seconds if missing
        
        char_data = result.get("character", {})
        current_hp = char_data.get("hp", 0)
        max_hp = char_data.get("max_hp", 0)
        
        print(f"Cooldown: {cooldown_seconds} seconds")
        time.sleep(cooldown_seconds)
        print(f"Health: {current_hp}/{max_hp}")
        if current_hp < max_hp:
            print("Health is below maximum. Resting...")
            rest_result = api.rest()
            if rest_result:
                rest_cooldown = rest_result.get("cooldown", {}).get("total_seconds", 5)
                time.sleep(rest_cooldown)
                print("Rested")
        else:
            print("Health is full. Continuing to fight...")
            time.sleep(cooldown_seconds)
