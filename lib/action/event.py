""" This module represents specific game events. """

from typing import List, Tuple, Any
import pygame
from pygame.surface import Surface
from lib.environment.shape import Shape


def game_event() -> List:
    return pygame.event.get()


def pump_event() -> None:
    return pygame.event.pump()


def init_game() -> None:
    pygame.init()


def pressed_mouse() -> List:
    return pygame.mouse.get_pressed()


def mouse_position() -> List:
    return pygame.mouse.get_pos()


def draw_ellipse(surface: Surface, color: Tuple, width: int) -> None:
    pygame.draw.ellipse(surface, color, surface.get_rect(), width)


def smooth_scale(surface: Surface, rect: Shape) -> Any:
    return pygame.transform.smoothscale(surface, [int(min(rect.size) * 0.5)] * 2)
