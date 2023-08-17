import random

from src.constants import SQUARE_HEIGHT, SQUARE_WIDTH


def generate_position(start=5, end=20):
    x, y = (
        random.randint(start, end) * SQUARE_WIDTH,
        random.randint(start, end) * SQUARE_HEIGHT
    )
    return x, y
