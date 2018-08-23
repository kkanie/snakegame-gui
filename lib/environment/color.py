from abc import ABC, abstractmethod
from typing import Iterable
from pygame import Color


class EnvColor(ABC):
    """Abstract color interface."""

    @abstractmethod
    def get(self) -> int:
        pass


class GameColor(EnvColor):
    """Engine color interface."""

    def __init__(self, color: Iterable) -> None:
        self._color: Color = Color(*color)

    def get(self) -> Color:
        return self._color
