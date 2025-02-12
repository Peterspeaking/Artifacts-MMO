import threading
import time
import logging
import colorlog
from core.game_engine import GameEngine

def configure_logging():
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        "%(log_color)s [%(name)s] %(levelname)s:%(reset)s %(message)s",
        log_colors={
            'DEBUG':    'blue',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red,bg_white',
        }
    ))
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

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
    crafting_characters = ["MrSpeak"]
    fighting_characters = ["Honeycomb"]

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
    
