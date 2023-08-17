from typing import Type

from src.square import Shape
from src.utils import generate_position


def generate_apple(obj: Type[Shape], snake_tail: list[Shape]) -> Shape:
    position = generate_position()
    while position in [item.position for item in snake_tail]:
        position = generate_position()

    return obj(position, color="red")
