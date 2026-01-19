from __future__ import annotations

from pathlib import Path
from typing import List

from pydantic import BaseModel, Field, ValidationError


class Vec2(BaseModel):
    x: int = Field(..., ge=0)
    y: int = Field(..., ge=0)


class Coin(BaseModel):
    x: int = Field(..., ge=0)
    y: int = Field(..., ge=0)
    r: int = Field(..., ge=3, le=30)


class Wall(BaseModel):
    x: int = Field(..., ge=0)
    y: int = Field(..., ge=0)
    w: int = Field(..., gt=0)
    h: int = Field(..., gt=0)


class Level(BaseModel):
    width: int = Field(default=800, ge=320, le=1920)
    height: int = Field(default=600, ge=240, le=1080)
    player_start: Vec2
    coins: List[Coin]
    walls: List[Wall] = []


def load_level(path: str | Path) -> Level:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Level file not found: {p}")

    text = p.read_text(encoding="utf-8-sig")  # entfernt BOM automatisch
    return Level.model_validate_json(text)



__all__ = ["Level", "Vec2", "Coin", "Wall", "load_level", "ValidationError"]
