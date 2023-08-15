from constants import HEIGHT, WIDTH
from snake import Snake
from square import Shape


def wall_collision(snake: Snake) -> bool:
    x, y = snake.head.position
    return x >= WIDTH or x < 0 or y >= HEIGHT or y < 0


def apple_collision(apple: Shape, snake: Snake) -> bool:
    return apple.position == snake.position
