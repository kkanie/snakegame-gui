import sys
from abc import ABC, abstractmethod
from typing import List, Iterable, Callable, Tuple
from pygame.surface import Surface
from lib.action.event import (
    mouse_position, game_event,
    pump_event, pressed_mouse,
    draw_ellipse, smooth_scale,
    init_game
)
from lib.environment.color import GameColor
from lib.environment.font import GameFont
from lib.environment.control import Controls, GameControls
from lib.environment.screen import GameScreen, Screen
from lib.environment.image import Image, GameImage
from lib.environment.shape import Rectangle
from lib.snake.food import Apple, Food
from lib.snake.snake import Snake, SnakeEntity


class Engine(ABC):
    """Abstract interface for a game."""

    @abstractmethod
    def prepare_canvas(self) -> None:
        pass

    @abstractmethod
    def terminate(self) -> None:
        pass

    @abstractmethod
    def make_button(self, pos, text, color, action, text_size=20) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def loop(self) -> None:
        pass


class Menu(ABC):
    """Abstract interface for a menu game."""

    @abstractmethod
    def prepare_canvas(self) -> None:
        pass

    @abstractmethod
    def make_text(self, x: int, y: int, text: str, size: int=20, color: Tuple=(0, 0, 0), center: bool=False) -> None:
        pass

    @abstractmethod
    def make_button(self, loc: Iterable, text: str, color: Iterable, action: Callable, size: int=20) -> None:
        pass

    @abstractmethod
    def mainloop(self) -> None:
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

    @abstractmethod
    def easy(self) -> None:
        pass

    @abstractmethod
    def normal(self) -> None:
        pass

    @abstractmethod
    def advanced(self) -> None:
        pass

    @abstractmethod
    def expert(self) -> None:
        pass

    @abstractmethod
    def quit(self) -> None:
        pass


class Game(ABC):
    """Abstract interface for a game."""

    @abstractmethod
    def start(self, speed: float, size: int) -> None:
        pass

    @abstractmethod
    def restart(self) -> None:
        pass

    @abstractmethod
    def launch_main_menu(self) -> None:
        pass


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


class SnakeGameEngine(Engine):
    """Snake game engine."""

    def __init__(self, speed: float, size: int = 1) -> None:
        self._screen: Screen = GameScreen()
        self._snake: Snake = SnakeEntity(speed, size)
        self._controls: Controls = GameControls()
        self._blocks: List = []
        self._score: int = 0
        self._size: int = size
        self._left, self._right, self._up, self._down = False, False, False, False
        self._hover: bool = False
        self._click: bool = False
        self._button_click = None
        self._apple: Food = Apple(size)
        self.prepare_canvas()

    def prepare_canvas(self) -> None:
        for pict in range(0, 800, 10):
            image: Image = GameImage(location=(10, 10))
            image.fill(color=(0, 0, 0))
            self._blocks.append([image.surface(), [pict, 0]])
        for pict in range(0, 800, 10):
            image: Image = GameImage(location=(10, 10))
            image.fill(color=(0, 0, 0))
            self._blocks.append([image.surface(), [pict, 440]])
        for pict in range(0, 450, 10):
            image: Image = GameImage(location=(10, 10))
            image.fill(color=(0, 0, 0))
            self._blocks.append([image.surface(), [0, pict]])
        for pict in range(0, 450, 10):
            image: Image = GameImage(location=(10, 10))
            image.fill(color=(0, 0, 0))
            self._blocks.append([image.surface(), [790, pict]])

    def terminate(self) -> None:
        while True:
            for event in game_event():
                if event.type == self._controls.type().quit():
                    sys.exit()
            for block in self._blocks:
                self._screen.blit(block[0], block[1])

            text = GameFont('Courier New', 50, 'Game Over    Score:', True, (255, 255, 255)).render()
            txt_rect = text.get_rect()
            txt_rect.topleft = (20, 150)
            self._screen.blit(text, txt_rect)

            text = GameFont('Courier New', 50, str(self._snake.score()), True, (255, 255, 255)).render()
            txt_rect = text.get_rect()
            txt_rect.topleft = (600, 150)
            self._screen.blit(text, txt_rect)

            self._screen.update()
            self.make_button((153, 300, 100, 50),
                             'Restart', [(255, 255, 255), (150, 150, 150)],
                             action=PySnakeGame().restart)
            if self._hover:
                pump_event()
                click: List = pressed_mouse()
                if click[0] == 1:
                    self._click = True
                if self._click:
                    if click[0] == 0:
                        self._button_click()
                        self._click = False

    def make_button(self, loc: Iterable, text: str, color: Iterable, action: Callable, size=20):
        mouse = mouse_position()
        old_loc = loc
        rect = Rectangle(loc).shape()
        rect.topleft = 0, 0
        rectangle: Surface = GameImage(rect.size, self._controls.type().src_alpha()).surface()

        circle: Surface = GameImage([min(rect.size) * 3] * 2, self._controls.type().src_alpha()).surface()
        draw_ellipse(circle, (0, 0, 0), 0)
        circle = smooth_scale(circle, rect)

        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)

        rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
        rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))
        loc = old_loc
        if (loc[0] + loc[2]) > mouse[0] > loc[0] and (loc[1] + loc[3]) > mouse[1] > loc[1]:
            self._hover = True
            self._button_click = action
            color = GameColor(color[1]).get()
            alpha = color.a
            color.a = 0
        else:
            color = GameColor(color[0]).get()
            alpha = color.a
            color.a = 0
            self._hover = False
        rectangle.fill(color, special_flags=self._controls.type().blend_rgba_max())
        rectangle.fill((255, 255, 255, alpha), special_flags=self._controls.type().blend_rgba_min())
        self._screen.blit(rectangle, loc)
        txt = GameFont('Courier New', size, text, True, (0, 0, 0)).render()
        txt_rect = txt.get_rect()
        txt_rect.center = (loc[0] + loc[2] / 2), (loc[1] + loc[3] / 2)
        self._screen.blit(txt, txt_rect)

    def reset(self) -> None:
        self._left, self._right, self._up, self._down = False, False, False, False

    def loop(self) -> None:
        while True:
            self._screen.fill((35, 38, 117))
            self._snake.update()
            for block in self._blocks:
                if self._snake.verify_snake(block[1]):
                    self.terminate()
                self._screen.blit(block[0], block[1])
            counter: int = 0
            for block in self._snake.images():
                if counter != 0:
                    if self._snake.verify_apple(block[1]):
                        self.terminate()
                self._screen.blit(block[0], block[1])
                counter += 1
            if self._snake.verify_apple(self._apple.location()):
                self._snake.put_apple()
                del self._apple
                self._apple: Food = Apple(self._size)
            self._screen.blit(self._apple.image(), self._apple.location())
            self._screen.blit(self._snake.image(), self._snake.location())
            for event in game_event():
                if event.type == self._controls.type().quit():
                    sys.exit(0)
                elif event.type == self._controls.type().down():
                    if event.key == self._controls.key().escape():
                        sys.exit(0)
                    if event.key == self._controls.key().right():
                        if not self._left:
                            self.reset()
                            self._snake.move_right()
                            self._right = True
                    if event.key == self._controls.key().left():
                        if not self._right:
                            self.reset()
                            self._snake.move_left()
                            self._left = True
                    if event.key == self._controls.key().up():
                        if not self._down:
                            self.reset()
                            self._snake.move_up()
                            self._up = True
                    if event.key == self._controls.key().down():
                        if not self._up:
                            self.reset()
                            self._snake.move_down()
                            self._down = True
            self._screen.update()


class StartGameMenu(Menu):
    """Start game menu interface."""

    def __init__(self):
        self._game: Game = PySnakeGame()
        self._controls: Controls = GameControls()
        self._screen: Screen = GameScreen()
        self._run_button = '(150, 300,100,50),"Run", [(0,255,0), (0,150,0)], action = self.start_up'
        self._quit_button = '(550, 300,100,50),"Quit", [(255,0,0), (150,0,0)], action = self.quit'
        self._hard_button, self._expert_button = None, None
        self._buttons = [self._run_button, self._quit_button]
        self._button_click = None
        self._hover = None
        self._blocks = []
        self._size = 1
        self._click, self._loads = False, False
        self.prepare_canvas()

    def prepare_canvas(self) -> None:
        for pict in range(0, 800, 10):
            image: Image = GameImage(location=(10, 10))
            image.fill(color=(0, 0, 0))
            self._blocks.append([image.surface(), [pict, 0]])
        for pict in range(0, 800, 10):
            image: Image = GameImage(location=(10, 10))
            image.fill(color=(0, 0, 0))
            self._blocks.append([image.surface(), [pict, 440]])
        for pict in range(0, 450, 10):
            image: Image = GameImage(location=(10, 10))
            image.fill(color=(0, 0, 0))
            self._blocks.append([image.surface(), [0, pict]])
        for pict in range(0, 450, 10):
            image: Image = GameImage(location=(10, 10))
            image.fill(color=(0, 0, 0))
            self._blocks.append([image.surface(), [790, pict]])

    def make_text(self, x: int, y: int, text: str, size: int=20, color: Tuple=(0, 0, 0), center: bool=False) -> None:
        txts = GameFont('Courier New', size, text, True, color).render()
        txtrect = txts.get_rect()
        txtrect.topleft = x, y
        if center:
            txtrect.center = x, y
        self._screen.blit(txts, txtrect)

    def make_button(self, loc: Iterable, text: str, color: Iterable, action: Callable, size: int=20) -> None:
        mouse = mouse_position()
        oldpos = loc
        rect = Rectangle(loc).shape()
        rect.topleft = 0, 0
        rectangle: Surface = GameImage(rect.size, self._controls.type().src_alpha()).surface()

        circle: Surface = GameImage([min(rect.size) * 3] * 2, self._controls.type().src_alpha()).surface()
        draw_ellipse(circle, (0, 0, 0), 0)
        circle = smooth_scale(circle, rect)

        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)

        rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
        rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))
        loc = oldpos
        if (loc[0] + loc[2]) > mouse[0] > loc[0] and (loc[1] + loc[3]) > mouse[1] > loc[1]:
            self._hover = True
            self._button_click = action
            color = GameColor(color[1]).get()
            alpha = color.a
            color.a = 0
        else:
            color = GameColor(color[0]).get()
            alpha = color.a
            color.a = 0
            self._hover = False
        rectangle.fill(color, special_flags=self._controls.type().blend_rgba_max())
        rectangle.fill((255, 255, 255, alpha), special_flags=self._controls.type().blend_rgba_min())
        self._screen.blit(rectangle, loc)
        self.make_text((loc[0] + loc[2] / 2), (loc[1] + loc[3] / 2), text, center=True, size=size)

    def mainloop(self) -> None:
        while True:
            self._screen.fill((35, 38, 117))
            self.make_text(400, 150, 'PySnake Game', color=(255, 255, 255), size=80, center=True)
            for event in game_event():
                if event.type == self._controls.type().quit():
                    sys.exit()
            for block in self._blocks:
                self._screen.blit(block[0], block[1])
            for button in self._buttons:
                exec('self.make_button({})'.format(button))
                if self._hover:
                    pump_event()
                    click = pressed_mouse()
                    if click[0] == 1:
                        self._click = True
                    if self._click:
                        if click[0] == 0:
                            self._button_click()
                            self._click = False
            self._screen.update()

    def start_up(self) -> None:
        self._run_button: str = '(150,300,100,50),"Small", [(0,255,0), (0,150,0)], self.small'
        self._quit_button: str = '(550,300,100,50),"Huge", [(0,255,0), (0,150,0)], self.huge'
        self._buttons: List = [self._run_button, self._quit_button]

    def small(self) -> None:
        self._run_button: str = '(150,300,100,50),"Easy", [(0,255,0), (0,150,0)], self.easy'
        self._quit_button: str = '(283,300,100,50),"Normal", [(0,255,0), (0,150,0)], self.normal'
        self._hard_button: str = '(417,300,100,50),"Advanced", [(0,255,0), (0,150,0)], self.advanced'
        self._expert_button: str = '(550,300,100,50),"Expert", [(0,255,0), (0,150,0)], self.expert'
        self._buttons: List = [self._run_button, self._quit_button, self._hard_button, self._expert_button]

    def huge(self) -> None:
        self._size = 2
        self._run_button: str = '(150,300,100,50),"Easy", [(0,255,0), (0,150,0)], self.easy'
        self._quit_button: str = '(283,300,100,50),"Normal", [(0,255,0), (0,150,0)], self.normal'
        self._hard_button: str = '(417,300,100,50),"Advanced", [(0,255,0), (0,150,0)], self.advanced'
        self._expert_button: str = '(550,300,100,50),"Expert", [(0,255,0), (0,150,0)], self.expert'
        self._buttons: List = [self._run_button, self._quit_button, self._hard_button, self._expert_button]

    def easy(self) -> None:
        self._game.start(1, self._size)

    def normal(self) -> None:
        self._game.start(1.5, self._size)

    def advanced(self) -> None:
        self._game.start(2, self._size)

    def expert(self) -> None:
        self._game.start(3, self._size)

    def quit(self) -> None:
        sys.exit(0)


class PySnakeGame(Game):
    """Snake game interface."""

    def start(self, speed: float, size: int) -> None:
        global game, menu
        del menu

        game = SnakeGameEngine(speed, size)
        game.loop()

    def restart(self) -> None:
        global game
        del game
        self.launch_main_menu()

    def launch_main_menu(self) -> None:
        global menu
        init_game()
        menu = StartGameMenu()
        menu.mainloop()
