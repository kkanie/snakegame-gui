import pytest
from lib.environment.buttons import Buttons, GameButtons


@pytest.fixture(scope='module')
def buttons() -> Buttons:
    return GameButtons()


def test_initial_buttons(buttons: Buttons) -> None:
    assert len(buttons.elements()) == 2


def test_start_up_buttons(buttons: Buttons) -> None:
    buttons.start_up()
    assert len(buttons.elements()) == 2


def test_small_buttons(buttons: Buttons) -> None:
    buttons.small()
    assert len(buttons.elements()) == 4


def test_huge_buttons(buttons: Buttons) -> None:
    buttons.huge()
    assert len(buttons.elements()) == 4
