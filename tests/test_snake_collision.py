import pytest

from src.snake import Snake
from src.snake_collision import wall_collision, apple_collision
from src.square import Square


@pytest.fixture(scope='function')
def snake(request):
    return Snake(request.param, obj_type=Square)


@pytest.fixture(scope='function')
def apple(request):
    return Square(request.param)


@pytest.mark.parametrize(
    "snake, result", [((100, 100), False), ((-20, 100), True)], indirect=['snake']
)
def test_wall_collision(snake, result):
    assert wall_collision(snake) is result


@pytest.mark.parametrize(
    "snake, apple, result",
    [
        ((100, 100), (100, 100), True),
        ((200, 100), (170, 100), True),
        ((260, 130), (100, 130), False),
        ((260, 130), (170, 130), True),
    ],
    indirect=['snake', 'apple']
)
def test_apple_collision(snake, apple, result):
    assert apple_collision(apple, snake) is result
