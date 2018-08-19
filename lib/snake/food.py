from abc import ABC, abstractmethod
from random import randrange
from typing import List
from lib.environment.surface import Image, GameImage
from pygame import Surface


class Food(ABC):
    """Abstract interface for food."""

    @abstractmethod
    def location(self) -> List[int]:
        pass

    @abstractmethod
    def image(self) -> Surface:
        pass


class Apple(Food):
    """Apple food interface."""

    def __init__(self, size: int) -> None:
        self._image: Image = GameImage(location=(10 * size, 10 * size), color=(255, 0, 0))
        self._location: List[int] = [randrange(10, 700, 20), randrange(10, 400, 20)]

    def location(self) -> List[int]:
        return self._location

    def image(self) -> Surface:
        return self._image.surface()
