""" This module represents specific game events. """

from typing import List
import pygame


def game_event() -> List:
    return pygame.event.get()


def pump_event() -> None:
    return pygame.event.pump()


def pressed_mouse() -> List:
    return pygame.mouse.get_pressed()


def mouse_position() -> List:
    return pygame.mouse.get_pos()
