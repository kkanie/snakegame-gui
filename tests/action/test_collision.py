from typing import List
import pytest
from lib.action.collision import GameCollision, Collision

_position: List[int] = [1, 2]
_size: int = 2
_location: List[int] = [1, 2]


@pytest.fixture(scope='module')
def collision() -> Collision:
    return GameCollision(_position, _size)


def test_collision_snake(collision: Collision) -> None:
    assert collision.snake(_location)


def test_collision_apple(collision: Collision) -> None:
    assert collision.apple(_location)
