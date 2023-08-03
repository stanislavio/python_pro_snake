from dataclasses import dataclass, field

import pygame as pg

from constants import SQUARE_WIDTH, SQUARE_HEIGHT
from square import Square


@dataclass
class Snake:

    position: tuple[int, int]
    tail: list[Square] = field(default_factory=list)

    head: Square = None

    def __post_init__(self):
        self.head = Square(self.position, (SQUARE_WIDTH, SQUARE_HEIGHT))
        self.tail.append(self.head)

    def draw(self, screen):
        for square in self.tail:
            square.draw(screen)

    def move(self, key):
        x, y = self.position
        if key == pg.K_UP:
            y -= SQUARE_HEIGHT
        if key == pg.K_DOWN:
            y += SQUARE_HEIGHT
        if key == pg.K_RIGHT:
            x += SQUARE_WIDTH
        if key == pg.K_LEFT:
            x -= SQUARE_WIDTH
        self.position = (x, y)
        print(f'My position {self.position}')
        self.head.position = self.position
