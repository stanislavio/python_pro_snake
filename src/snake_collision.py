from src.constants import HEIGHT, WIDTH
from src.snake import Snake
from src.square import Shape


def wall_collision(snake: Snake) -> bool:
    x, y = snake.head.position
    return x >= WIDTH or x < 0 or y >= HEIGHT or y < 0


def apple_collision(apple: Shape, snake: Snake) -> bool:
    return any(apple.position == item.position for item in snake.tail)
