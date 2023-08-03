from dataclasses import dataclass

import pygame as pg

from constants import SQUARE_WIDTH, SQUARE_HEIGHT


@dataclass
class Square:

    position: tuple[int, int]
    size: tuple[int, int] = (SQUARE_WIDTH, SQUARE_HEIGHT)

    color: str = 'green'

    def draw(self, screen):
        pg.draw.rect(screen, self.color, pg.Rect(*self.position, *self.size))
