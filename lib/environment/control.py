from abc import ABC, abstractmethod
from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE, KEYDOWN, QUIT


class Key(ABC):
    """Abstract interface for a game control key."""

    @abstractmethod
    def right(self) -> int:
        pass

    @abstractmethod
    def left(self) -> int:
        pass

    @abstractmethod
    def down(self) -> int:
        pass

    @abstractmethod
    def up(self) -> int:
        pass

    @abstractmethod
    def escape(self) -> int:
        pass


class Type(ABC):
    """Abstract interface for control type."""

    @abstractmethod
    def down(self) -> int:
        pass

    @abstractmethod
    def quit(self) -> int:
        pass


class Controls(ABC):
    """Abstract factory for game controls."""

    @abstractmethod
    def key(self) -> Key:
        pass

    @abstractmethod
    def type(self) -> Type:
        pass


class ControlKey(Key):
    """Key game control."""

    def __init__(self) -> None:
        self._right: int = K_RIGHT
        self._left: int = K_LEFT
        self._up: int = K_UP
        self._down: int = K_DOWN
        self._escape: int = K_ESCAPE

    def right(self) -> int:
        return self._right

    def left(self) -> int:
        return self._left

    def down(self) -> int:
        return self._down

    def up(self) -> int:
        return self._up

    def escape(self) -> int:
        return self._escape


class ControlType(Type):
    """Type game control."""

    def __init__(self) -> None:
        self._quit: int = QUIT
        self._down: int = KEYDOWN

    def down(self) -> int:
        return self._down

    def quit(self) -> int:
        return self._quit


class GameControls(Controls):
    """Concrete game controls."""

    def __init__(self) -> None:
        self._key: Key = ControlKey()
        self._type: Type = ControlType()

    def key(self) -> Key:
        return self._key

    def type(self) -> Type:
        return self._type
