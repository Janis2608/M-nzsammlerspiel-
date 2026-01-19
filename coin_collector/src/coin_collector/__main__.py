from __future__ import annotations

import typer

from .config import load_level
from .game import run_game

app = typer.Typer(add_completion=False)


@app.callback(invoke_without_command=True)
def main(
    level: str = typer.Option(..., "--level"),
    fps: int = typer.Option(60, "--fps"),
    debug: bool = typer.Option(False, "--debug"),
):
    print(">>> __main__.py started")
    print(">>> args:", level, fps, debug)

    lvl = load_level(level)
    print(">>> level loaded OK -> starting run_game()")

    run_game(lvl, fps=fps, debug=debug)
    print(">>> run_game returned (game closed)")


if __name__ == "__main__":
    app()
