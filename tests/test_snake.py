import unittest

from src.snake import Snake
from src.square import Square


class TestSnake(unittest.TestCase):

    def setUp(self) -> None:
        self.snake = Snake((100, 100), Square, min_len=1)

    def tearDown(self) -> None:
        del self.snake

    def test_init(self):
        self.assertEqual(self.snake.position, (100, 100))

    def test_tail(self):

        self.assertEqual(
            self.snake.tail,
            [Square((100, 100)), Square((70, 100))]
        )

