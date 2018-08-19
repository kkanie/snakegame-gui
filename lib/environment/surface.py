from abc import ABC, abstractmethod
from typing import Tuple
from pygame import Surface


class Image(ABC):
    """Abstract interface for an surface."""

    @abstractmethod
    def surface(self) -> Surface:
        pass


class GameImage(Image):
    """Specific game surface."""

    def __init__(self, location: Tuple, color: Tuple) -> None:
        self._surface: Surface = Surface(location)
        self._color: Tuple = color

    def surface(self) -> Surface:
        self._surface.fill(self._color)
        return self._surface
