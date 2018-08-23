import sys
from abc import ABC, abstractmethod
from typing import List, Iterable
from lib.snake.game import Game, PySnakeGame


class Buttons(ABC):
    """Buttons abstract interface."""

    @abstractmethod
    def elements(self) -> Iterable:
        pass

    @abstractmethod
    def start_up(self) -> None:
        pass

    @abstractmethod
    def small(self) -> None:
        pass

    @abstractmethod
    def huge(self) -> None:
        pass


class GameButtons(Buttons):
    """Game buttons interface."""

    def __init__(self) -> None:
        self._game: Game = PySnakeGame()
        self._run_button = '(150, 300,100,50),"Run", [(0,255,0), (0,150,0)], action = self.start_up'
        self._quit_button = '(550, 300,100,50),"Quit", [(255,0,0), (150,0,0)], action = self.quit'
        self._hard_button, self._expert_button = None, None
        self._buttons = [self._run_button, self._quit_button]
        self._size = 1

    def elements(self) -> Iterable:
        return self._buttons

    def start_up(self) -> None:
        self._run_button: str = '(150,300,100,50),"Small", [(0,255,0), (0,150,0)], action = self.small'
        self._quit_button: str = '(550,300,100,50),"Huge", [(0,255,0), (0,150,0)], action = self.huge'
        self._buttons: List = [self._run_button, self._quit_button]

    def small(self) -> None:
        self._run_button: str = '(150,300,100,50),"Easy", [(0,255,0), (0,150,0)], action = self.easy'
        self._quit_button: str = '(283,300,100,50),"Normal", [(0,255,0), (0,150,0)], self.normal'
        self._hard_button: str = '(417,300,100,50),"Advanced", [(0,255,0), (0,150,0)], action = self.advanced'
        self._expert_button: str = '(550,300,100,50),"Expert", [(0,255,0), (0,150,0)], action = self.expert'
        self._buttons: List = [self._run_button, self._quit_button, self._hard_button, self._expert_button]

    def huge(self) -> None:
        self._size = 2
        self._run_button: str = '(150,300,100,50),"Easy", [(0,255,0), (0,150,0)], action = self.easy'
        self._quit_button: str = '(283,300,100,50),"Normal", [(0,255,0), (0,150,0)], self.normal'
        self._hard_button: str = '(417,300,100,50),"Advanced", [(0,255,0), (0,150,0)], action = self.advanced'
        self._expert_button: str = '(550,300,100,50),"Expert", [(0,255,0), (0,150,0)], action = self.expert'
        self._buttons: List = [self._run_button, self._quit_button, self._hard_button, self._expert_button]

    def easy(self) -> None:
        self._game.start(1, self._size)

    def normal(self) -> None:
        self._game.start(1.5, self._size)

    def advanced(self) -> None:
        self._game.start(2, self._size)

    def expert(self) -> None:
        self._game.start(3, self._size)

    def stop(self) -> None:
        sys.exit(0)
