import logging
import colorlog

ANSI_COLOR_CODES = {
    "cyan": "\033[36m",
    "magenta": "\033[35m",
    "blue": "\033[34m",
    "yellow": "\033[33m",
    "light_red": "\033[91m",
    "light_blue": "\033[94m",
    "white": "\033[97m",
    "light_green": "\033[92m"
}

CHARACTER_COLOR_MAP = {}

def get_character_color(character: str):
    if character not in CHARACTER_COLOR_MAP:
        index = len(CHARACTER_COLOR_MAP) % len(ANSI_COLOR_CODES)
        color_name = list(ANSI_COLOR_CODES.keys())[index]
        CHARACTER_COLOR_MAP[character] = ANSI_COLOR_CODES[color_name]
    return CHARACTER_COLOR_MAP[character]

def configure_logging():
    handler = colorlog.StreamHandler()

    class CharacterColorFormatter(colorlog.ColoredFormatter):
        def format(self, record):
            char_name = record.name
            char_color = get_character_color(char_name)
            record.char_name_colored = f"{char_color}[{char_name}]\033[0m"

            return super().format(record)

    handler.setFormatter(CharacterColorFormatter(
        "%(char_name_colored)s %(log_color)s%(levelname)s:%(reset)s %(message)s",
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
