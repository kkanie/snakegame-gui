from abc import ABC, abstractmethod
from typing import Tuple, Iterable
import pygame
from pygame import Surface
from pygame.rect import Rect


class Screen(ABC):
    """Abstract interface for a screen."""

    @abstractmethod
    def fill(self, color: Tuple[int, int, int]) -> None:
        pass

    @abstractmethod
    def blit(self, surface: Surface, coordinate: Iterable) -> Rect:
        pass

    @abstractmethod
    def update(self) -> None:
        pass


class GameScreen(Screen):
    """Engine screen interface."""

    def __init__(self, resolution: Tuple[int, int] = (800, 450), title: str = 'PySnake Game') -> None:
        self._screen: Surface = pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)

    def fill(self, color: Tuple[int, int, int]) -> None:
        return self._screen.fill(color)

    def blit(self, surface: Surface, coordinate: Iterable) -> Rect:
        return self._screen.blit(surface, coordinate)

    def update(self) -> None:
        pygame.display.update()
