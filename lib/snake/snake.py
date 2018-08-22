from abc import ABC, abstractmethod
from typing import List
from pygame import Surface
from lib.action.collision import Collision, GameCollision
from lib.environment.image import GameImage, Image


class Snake(ABC):
    """Abstract interface for a snake."""

    @abstractmethod
    def score(self) -> int:
        pass

    @abstractmethod
    def image(self) -> Surface:
        pass

    @abstractmethod
    def images(self) -> List:
        pass

    @abstractmethod
    def location(self) -> List:
        pass

    @abstractmethod
    def move_right(self) -> None:
        pass

    @abstractmethod
    def move_left(self) -> None:
        pass

    @abstractmethod
    def move_up(self) -> None:
        pass

    @abstractmethod
    def move_down(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def verify_snake(self, location: List) -> bool:
        pass

    @abstractmethod
    def verify_apple(self, location: List) -> bool:
        pass

    @abstractmethod
    def put_apple(self) -> None:
        pass


class GreenSnake(Snake):
    """Concrete snake entity."""

    def __init__(self, speed: float, size: int) -> None:
        self._location: List = [20, 20]
        self._collision: Collision = GameCollision(self._location, size)
        self._image = GameImage(location=(10 * size, 10 * size))
        self._speed: float = speed
        self._size: int = size
        self._images: List = []
        self._old_position: List = [[20, 20]]
        self._direction: List = [0, 0]
        self._times: int = -11
        self._score: int = 0

    def score(self) -> int:
        return self._score

    def image(self) -> Surface:
        self._image.fill(color=(0, 255, 0))
        return self._image.surface()

    def images(self) -> List:
        return self._images

    def location(self) -> List:
        return self._location

    def move_right(self) -> None:
        self._direction = [self._speed, 0]

    def move_left(self) -> None:
        self._direction = [-self._speed, 0]

    def move_up(self) -> None:
        self._direction = [0, -self._speed]

    def move_down(self) -> None:
        self._direction = [0, self._speed]

    def update(self) -> None:
        if self._old_position[-1] != self._location:
            self._old_position.append([self._location[0], self._location[1]])
        self._location[0] += self._direction[0]
        self._location[1] += self._direction[1]
        image_counter: int = 1
        for image in self._images:
            image[1] = self._old_position[int(image_counter * ((self._times * self._size) / self._speed))]
            image_counter += 1

    def verify_snake(self, location: List) -> bool:
        return self._collision.snake(location)

    def verify_apple(self, location: List) -> bool:
        return self._collision.apple(location)

    def put_apple(self) -> None:
        self._score += 1
        image: Image = GameImage(location=(10 * self._size, 10 * self._size))
        image.fill(color=(0, 255, 0))
        self._images.append([image.surface(), [10, 10]])
