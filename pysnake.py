from lib.snake.game import Game, PySnakeGame


def _start_game() -> None:
    """Starts `PySnake` game runner."""
    game: Game = PySnakeGame()
    game.launch_main_menu()


if __name__ == '__main__':
    _start_game()

