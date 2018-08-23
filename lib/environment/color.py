from abc import ABC, abstractmethod
from typing import Iterable
from pygame import Color


class EnvColor(ABC):
    """Abstract color interface."""

    @abstractmethod
    def alpha(self) -> int:
        pass


class GameColor(EnvColor):
    """Game color interface."""

    def __init__(self, color: Iterable) -> None:
        self._color: Color = Color(*color)

    @property
    def alpha(self) -> int:
        return self._color.a

    @alpha.setter
    def alpha(self, value: int) -> None:
        self._color.a = value
