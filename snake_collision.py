from snake import Snake

from constants import WIDTH, HEIGHT
from square import Square, Shape


def wall_collision(snake: Snake) -> bool:
    x, y = snake.head.position
    return x >= WIDTH or x < 0 or y >= HEIGHT or y < 0


def apple_collision(apple: Shape, snake: Snake) -> bool:
    return apple.position == snake.position
