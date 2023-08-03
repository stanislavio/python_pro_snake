import random

from constants import SQUARE_WIDTH, SQUARE_HEIGHT


def generate_position():
    x, y = random.randint(0, 29) * SQUARE_WIDTH, random.randint(0, 24) * SQUARE_HEIGHT
    return x, y