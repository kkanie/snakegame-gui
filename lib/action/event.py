from abc import ABC, abstractmethod
from typing import List
import pygame


class Event(ABC):
    """Abstract interface for an event."""

    @abstractmethod
    def get(self) -> List:
        pass


class GameEvent(Event):
    """Game event interface."""

    def __init__(self) -> None:
        self._events = pygame.event

    def get(self) -> List:
        return self._events.get()
