import pygame
from constants import *


class HealthBar:
    def __init__(self, max_health=PLAYER_MAX_HEALTH):
        self.max_health = max_health

    def render(self, screen, current_health, x=HEALTH_BAR_X, y=HEALTH_BAR_Y_OFFSET):
        # Clamp health
        current_health = max(0, current_health)

        # -------------------------
        # Heart-based rendering
        # -------------------------
        total_hearts = self.max_health // HP_PER_HEART
        heart_width = HEALTH_BAR_WIDTH // total_hearts  # ⬅ to be added

        for i in range(total_hearts):
            heart_x = x + i * heart_width

            # HP remaining for this heart
            hp_left = current_health - (i * HP_PER_HEART)
            fill_ratio = max(0, min(HP_PER_HEART, hp_left)) / HP_PER_HEART
            fill_width = int(heart_width * fill_ratio)

            # Heart border
            pygame.draw.rect(
                screen,
                COLOR_UI_TEXT,
                (heart_x, y, heart_width, HEALTH_BAR_HEIGHT),
                HEALTH_BAR_BORDER_WIDTH  # ⬅ to be added
            )

            # Heart fill (supports half-heart)
            if fill_width > 0:
                pygame.draw.rect(
                    screen,
                    COLOR_UI_HEALTH,
                    (heart_x, y, fill_width, HEALTH_BAR_HEIGHT)
                )
