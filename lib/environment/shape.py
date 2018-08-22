from abc import ABC, abstractmethod
from typing import Tuple, Any, List
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
    def size(self) -> Tuple:
        pass


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, position: List) -> None:
        self._shape: Rect = Rect(position)
        self._top_left: Tuple = (0, 0)

    @abstractmethod
    def shape(self) -> Rect:
        return self._shape

    @property
    def top_left(self) -> Tuple:
        return self._top_left

    @top_left.setter
    def top_left(self, position: Tuple) -> None:
        self._top_left = position

    @property
    def size(self) -> Tuple:
        return self._shape.size
