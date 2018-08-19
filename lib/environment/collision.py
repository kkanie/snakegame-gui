from abc import ABC, abstractmethod
from typing import List


class Collision(ABC):
    """Abstract interface for a game collision."""

    @abstractmethod
    def snake(self, location: List) -> bool:
        pass

    @abstractmethod
    def apple(self, location: List) -> bool:
        pass


class GameCollision(Collision):
    """GreenSnake game collision interface."""

    def __init__(self, position: List, size: int) -> None:
        self._position: List = position
        self._size: int = size
        self._times: int = 11
        self._diff: int = 10
        self._shift: int = 1

    def snake(self, location: List) -> bool:
        return (location[0] + location[0] + self._diff) > self._position[0] > location[0] and \
               (location[1] + location[1] + self._diff) > self._position[1] > location[1] or \
               (location[0] + location[0] + self._diff) > self._position[0] + self._diff > location[0] and \
               (location[1] + location[1] + self._diff) > self._position[1] + self._diff > location[1]

    def apple(self, location: List) -> bool:
        return (location[0] - self._shift +
                (self._times * self._size)) > self._position[0] > location[0] - self._shift and \
               (location[1] - self._shift +
                (self._times * self._size)) > self._position[1] > location[1] - self._shift or \
               (location[0] - self._shift +
                (self._times * self._size)) > self._position[0] + self._diff > location[0] - self._shift and \
               (location[1] - self._shift +
                (self._times * self._size)) > self._position[1] + self._diff > location[1] - self._shift
