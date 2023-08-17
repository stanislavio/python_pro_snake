"""
This module is for Snake template class
"""

from dataclasses import dataclass, field
from typing import Type

from src.constants import SQUARE_HEIGHT, SQUARE_WIDTH
from src.square import Shape


@dataclass
class Snake:
    position: tuple[int, int]
    obj_type: Type[Shape]
    tail: list[Shape] = field(default_factory=list)
    vector: str = "RIGHT"
    min_len: int = 3
    alive: bool = True
    speed: int = 0
    speed_limit: float = 20

    head: Shape = None

    def __post_init__(self):
        self.head = self.obj_type(self.position, (SQUARE_WIDTH, SQUARE_HEIGHT))
        self.tail.append(self.head)
        self.generate_tail()

    def generate_tail(self):
        x, y = self.position
        for idx in range(1, self.min_len + 1):
            if self.vector == "RIGHT":
                self.tail.append(self.obj_type((x - idx * SQUARE_WIDTH, y)))
            if self.vector == "LEFT":
                self.tail.append(self.obj_type((x + idx * SQUARE_WIDTH, y)))
            if self.vector == "DOWN":
                self.tail.append(self.obj_type((x, y - idx * SQUARE_HEIGHT)))
            if self.vector == "UP":
                self.tail.append(self.obj_type((x, y + idx * SQUARE_HEIGHT)))

    def eat(self):
        self.tail.append(self.obj_type(self.tail[-1].position))

    def draw(self, screen):
        for square in self.tail:
            square.draw(screen)

    def _collision_myself(self):
        for item in self.tail[3:]:
            if item.position == self.position:
                self.alive = False
                break

    def move(self):
        x, y = self.position
        if self.vector == "UP":
            y -= SQUARE_HEIGHT
        if self.vector == "DOWN":
            y += SQUARE_HEIGHT
        if self.vector == "RIGHT":
            x += SQUARE_WIDTH
        if self.vector == "LEFT":
            x -= SQUARE_WIDTH

        self.position = (x, y)
        self._collision_myself()
        for idx in reversed(range(1, len(self.tail))):
            self.tail[idx].position = self.tail[idx - 1].position
        self.head.position = self.position
