import threading
import time
import logging
from core.game_engine import GameEngine
from core.logger_config import configure_logging

def crafting_loop(character: str):
    engine = GameEngine(character)
    while True:
        engine.perform_crafting_copper()

def fighting_loop(character: str):
    engine = GameEngine(character)
    while True:
        engine.perform_fight_cycle()

if __name__ == "__main__":
    configure_logging()

    crafting_characters = ["MrSpeak", "Honeycomb", "POSTmaster", "Miss200OK", "404"]
    fighting_characters = []

    threads = []
    for char in crafting_characters:
        t = threading.Thread(target=crafting_loop, args=(char,), name=char, daemon=True)
        t.start()
        threads.append(t)
    for char in fighting_characters:
        t = threading.Thread(target=fighting_loop, args=(char,), name=char, daemon=True)
        t.start()
        threads.append(t)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
