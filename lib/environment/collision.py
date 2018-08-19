from abc import ABC, abstractmethod
from typing import List


class Collision(ABC):
    """Abstract interface for a game collision."""

    @abstractmethod
    def snake(self, coord: List) -> bool:
        pass

    @abstractmethod
    def apple(self, coord: List) -> bool:
        pass


class GameCollision(Collision):
    """Snake game collision interface."""

    def __init__(self, position: List, size: int) -> None:
        self._position: List = position
        self._size: int = size
        self._times: int = 11
        self._diff: int = 10
        self._shift: int = 1

    def snake(self, coord: List) -> bool:
        return (coord[0] + coord[0] + self._diff) > self._position[0] > coord[0] and \
               (coord[1] + coord[1] + self._diff) > self._position[1] > coord[1] or \
               (coord[0] + coord[0] + self._diff) > self._position[0] + self._diff > coord[0] and \
               (coord[1] + coord[1] + self._diff) > self._position[1] + self._diff > coord[1]

    def apple(self, coordinate: List) -> bool:
        return (coordinate[0] - self._shift +
                (self._times * self._size)) > self._position[0] > coordinate[0] - self._shift and \
               (coordinate[1] - self._shift +
                (self._times * self._size)) > self._position[1] > coordinate[1] - self._shift or \
               (coordinate[0] - self._shift +
                (self._times * self._size)) > self._position[0] + self._diff > coordinate[0] - self._shift and \
               (coordinate[1] - self._shift +
                (self._times * self._size)) > self._position[1] + self._diff > coordinate[1] - self._shift

