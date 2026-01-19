from __future__ import annotations

import pygame

from .config import Level


def draw_world(
    screen: pygame.Surface,
    level: Level,
    player_rect: pygame.Rect,
    coin_rects: list[pygame.Rect],
    wall_rects: list[pygame.Rect],
    score: int,
    debug: bool,
    font: pygame.font.Font,
    fps_value: int,
) -> None:
    # Background
    screen.fill((25, 25, 30))

    # Walls
    for w in wall_rects:
        pygame.draw.rect(screen, (90, 90, 105), w)

    # Coins (circles based on rects)
    for c in coin_rects:
        center = c.center
        radius = c.width // 2
        pygame.draw.circle(screen, (255, 215, 0), center, radius)

    # Player
    pygame.draw.rect(screen, (90, 170, 255), player_rect)

    # HUD
    hud = f"Score: {score}   Remaining: {len(coin_rects)}"
    if debug:
        hud += f"   FPS: {fps_value}"
    img = font.render(hud, True, (240, 240, 240))
    screen.blit(img, (10, 10))

    # Debug outlines
    if debug:
        pygame.draw.rect(screen, (255, 80, 80), player_rect, 2)
        for c in coin_rects:
            pygame.draw.rect(screen, (255, 220, 80), c, 1)
        for w in wall_rects:
            pygame.draw.rect(screen, (80, 255, 120), w, 2)
