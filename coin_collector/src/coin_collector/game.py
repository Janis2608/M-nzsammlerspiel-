from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import time

import pygame

from .config import Level
from .draw import draw_world

PLAYER_SIZE = 32
PLAYER_SPEED = 240  # px/s


@dataclass
class GameResult:
    score: int
    collected_all: bool


def run_game(level: Level, fps: int = 60, debug: bool = False) -> GameResult:
    pygame.init()
    pygame.display.set_caption("Coin Collector")

    screen = pygame.display.set_mode((level.width, level.height))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    player = pygame.Rect(level.player_start.x, level.player_start.y, PLAYER_SIZE, PLAYER_SIZE)
    walls = [pygame.Rect(w.x, w.y, w.w, w.h) for w in level.walls]
    coins = [pygame.Rect(c.x - c.r, c.y - c.r, 2 * c.r, 2 * c.r) for c in level.coins]

    score = 0
    collected_all = False
    running = True

    while running:
        dt = clock.tick(fps) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_F12:
                    ts = time.strftime("%Y%m%d_%H%M%S")
                    filename = Path.cwd() / f"screenshot_{ts}.png"
                    pygame.image.save(screen, str(filename))
                    pygame.display.set_caption(f"Saved screenshot: {filename.name}")

        keys = pygame.key.get_pressed()
        vx = 0.0
        vy = 0.0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            vx -= 1.0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            vx += 1.0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            vy -= 1.0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            vy += 1.0

        # no diagonal speed advantage
        if vx != 0 and vy != 0:
            vx *= 0.7071
            vy *= 0.7071

        dx = int(vx * PLAYER_SPEED * dt)
        dy = int(vy * PLAYER_SPEED * dt)

        # move + collision
        player.x += dx
        for w in walls:
            if player.colliderect(w):
                if dx > 0:
                    player.right = w.left
                elif dx < 0:
                    player.left = w.right

        player.y += dy
        for w in walls:
            if player.colliderect(w):
                if dy > 0:
                    player.bottom = w.top
                elif dy < 0:
                    player.top = w.bottom

        # collect coins
        remaining = []
        for c in coins:
            if player.colliderect(c):
                score += 1
            else:
                remaining.append(c)
        coins = remaining

        # win
        if not collected_all and len(coins) == 0:
            collected_all = True
            pygame.display.set_caption("Alle Münzen eingesammelt! ESC zum Beenden.")

        draw_world(
            screen=screen,
            level=level,
            player_rect=player,
            coin_rects=coins,
            wall_rects=walls,
            score=score,
            debug=debug,
            font=font,
            fps_value=int(clock.get_fps()),
        )
        pygame.display.flip()

    pygame.quit()
    return GameResult(score=score, collected_all=collected_all)
