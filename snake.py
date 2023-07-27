import pygame as pg

from constants import SQUARE_WIDTH, SQUARE_HEIGHT


class Snake:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.head = pg.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HEIGHT)
        self.tail = []

    def draw(self, screen):
        screen.fill('purple')
        pg.draw.rect(screen, 'green', self.head)

    def move(self, key):
        if key == pg.K_UP:
            self.y -= SQUARE_HEIGHT
        if key == pg.K_DOWN:
            self.y += SQUARE_HEIGHT
        if key == pg.K_RIGHT:
            self.x += SQUARE_WIDTH
        if key == pg.K_LEFT:
            self.x -= SQUARE_WIDTH
        print(f'My position {self.x}, {self.y}')
        self.head = pg.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HEIGHT)
