import random

from constants import SQUARE_HEIGHT, SQUARE_WIDTH


def generate_position():
    x, y = random.randint(5, 24) * SQUARE_WIDTH, random.randint(5, 19) * SQUARE_HEIGHT
    return x, y
