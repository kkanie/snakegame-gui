from abc import ABC, abstractmethod
from typing import Tuple
from pygame import Surface


class Image(ABC):
    """Abstract interface for an fill."""

    @abstractmethod
    def fill(self, color: Tuple) -> None:
        pass

    @abstractmethod
    def surface(self) -> Surface:
        pass


class GameImage(Image):
    """Specific game fill."""

    def __init__(self, location: Tuple, *args) -> None:
        self._surface: Surface = Surface(location, *args)

    def fill(self, color: Tuple) -> None:
        self._surface.fill(color)

    def surface(self) -> Surface:
        return self._surface
