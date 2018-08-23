from abc import ABC, abstractmethod
from typing import Tuple, Iterable, Any
from pygame.rect import Rect


class Shape(ABC):
    """Abstract shape interface."""

    @abstractmethod
    def shape(self) -> Any:
        pass

    @abstractmethod
    def top_left(self) -> Tuple:
        pass

    @abstractmethod
    def top_right(self) -> Iterable:
        pass

    @abstractmethod
    def size(self) -> Tuple:
        pass

    @abstractmethod
    def bottom_right(self) -> Iterable:
        pass

    @abstractmethod
    def bottom_left(self) -> Iterable:
        pass

    @abstractmethod
    def inflate(self, x: int, y: int) -> Rect:
        pass


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, position: Iterable) -> None:
        self._shape: Rect = Rect(position)
        self._top_left: Tuple = (0, 0)

    def shape(self) -> Any:
        return self._shape

    @property
    def top_left(self) -> Tuple:
        return self._top_left

    @top_left.setter
    def top_left(self, position: Tuple) -> None:
        self._top_left = position

    @property
    def top_right(self) -> Iterable:
        return self._shape.topright

    @property
    def bottom_left(self) -> Iterable:
        return self._shape.bottomleft

    @property
    def bottom_right(self) -> Iterable:
        return self._shape.bottomright

    @property
    def size(self) -> Tuple:
        return self._shape.size

    def inflate(self, x: int, y: int) -> Rect:
        return self._shape.inflate(x, y)
