from abc import ABC, abstractmethod
from typing import Any, Tuple

import pygame


class Font(ABC):
    """Abstract interface for an event."""

    @abstractmethod
    def render(self) -> Any:
        pass


class GameFont(Font):
    """Game font interface."""

    def __init__(self, name: str, size: int, text: str, antialias: bool, color: Tuple) -> None:
        self._font = pygame.font.SysFont(name, size)
        self._text: str = text
        self._antialias: bool = antialias
        self._color: Tuple = color

    def render(self) -> Any:
        return self._font.render(self._text, self._antialias, self._color)
