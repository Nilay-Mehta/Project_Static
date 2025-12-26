import pygame
from constants import *


class HealthBar:
    def __init__(self, max_health=PLAYER_MAX_HEALTH):
        self.max_health = max_health

    def render(self, screen, current_health):
        bar_width = 200
        bar_height = 20
        x = 10
        y = SCREEN_HEIGHT - 30

        health_ratio = max(0, current_health) / self.max_health
        current_width = int(bar_width * health_ratio)

        pygame.draw.rect(screen, COLOR_UI_TEXT, (x, y, bar_width, bar_height), 2)
        pygame.draw.rect(screen, COLOR_UI_HEALTH, (x, y, current_width, bar_height))
