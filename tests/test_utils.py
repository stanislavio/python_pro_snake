import pytest

from src.constants import SQUARE_HEIGHT, SQUARE_WIDTH
from src.utils import generate_position


def randint(a, b):
    return a * b


@pytest.mark.parametrize(
    "start, end", [(2, 3), (4, 5), (20, 10)]
)
def test_generate_position(mocker, start, end):
    mocker.patch('random.randint', randint)
    result = generate_position(start, end)

    assert result == (
        SQUARE_WIDTH * randint(start, end),
        SQUARE_HEIGHT * randint(start, end)
    )
