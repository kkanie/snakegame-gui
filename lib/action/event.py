from abc import ABC, abstractmethod
from typing import List
import pygame


class Event(ABC):
    """Abstract interface for an event."""

    @abstractmethod
    def get(self) -> List:
        pass

    @abstractmethod
    def pump(self) -> None:
        pass

    @abstractmethod
    def mouse_pressed(self) -> List:
        pass


class GameEvent(Event):
    """Game event interface."""

    def __init__(self) -> None:
        self._events = pygame.event
        self._mouse = pygame.mouse

    def get(self) -> List:
        return self._events.get()

    def pump(self) -> None:
        self._events.pump()

    def mouse_pressed(self) -> List:
        return self._mouse.get_pressed()
