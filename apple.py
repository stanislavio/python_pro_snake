import random

from constants import SQUARE_WIDTH, SQUARE_HEIGHT
from square import Square
from utils import generate_position


def generate_apple(snake_tail: list[Square]) -> Square:
    position = generate_position()

    return Square(position, color='red')
