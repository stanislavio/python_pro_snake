from abc import ABC, abstractmethod
from dataclasses import dataclass

import pygame as pg

from constants import SQUARE_WIDTH, SQUARE_HEIGHT


@dataclass
class Shape(ABC):
    position: tuple[int, int]
    size: tuple[int, int] = (SQUARE_WIDTH, SQUARE_HEIGHT)

    color: str = 'green'

    @abstractmethod
    def draw(self, screen):
        raise NotImplemented


class Square(Shape):

    def draw(self, screen):
        w, h = self.size
        pg.draw.rect(screen, self.color, pg.Rect(*self.position, w - 1, h - 1))


class Circle(Shape):

    def draw(self, screen):
        w, h = self.size
        x, y = self.position
        center = x + w / 2, y + h / 2
        pg.draw.circle(screen, self.color, center, (w + h) / 4)


class Triangle(Shape):

    def draw(self, screen):
        x, y = self.position
        w, h = self.size
        points = ((x + w / 2, y), (x, y + h), (x + w, y + h))
        pg.draw.polygon(screen, self.color, points)
