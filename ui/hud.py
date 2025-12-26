import pygame
from constants import *


class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 20)

    def render(self, screen, player, weather):
        y_pos = 10

        health_text = self.font.render(
            f"Health: {int(player.health)}/{PLAYER_MAX_HEALTH}",
            True,
            COLOR_UI_HEALTH
        )
        screen.blit(health_text, (10, y_pos))
        y_pos += 25

        stamina_text = self.font.render(
            f"Stamina: {int(player.stamina)}",
            True,
            COLOR_UI_TEXT
        )
        screen.blit(stamina_text, (10, y_pos))
        y_pos += 25

        hunger_color = (
            COLOR_UI_RADIATION_LOW if player.hunger > 30
            else COLOR_UI_RADIATION_HIGH
        )
        hunger_text = self.font.render(
            f"Hunger: {int(player.hunger)}",
            True,
            hunger_color
        )
        screen.blit(hunger_text, (10, y_pos))
        y_pos += 25

        thirst_color = (
            COLOR_UI_RADIATION_LOW if player.thirst > 30
            else COLOR_UI_RADIATION_HIGH
        )
        thirst_text = self.font.render(
            f"Thirst: {int(player.thirst)}",
            True,
            thirst_color
        )
        screen.blit(thirst_text, (10, y_pos))
        y_pos += 25

        rad_percentage = (player.radiation / PLAYER_MAX_RADIATION) * 100

        if rad_percentage > 80:
            rad_color = COLOR_UI_RADIATION_HIGH
        elif rad_percentage > 50:
            rad_color = COLOR_UI_RADIATION_MED
        else:
            rad_color = COLOR_UI_RADIATION_LOW

        rad_text = self.font.render(
            f"Radiation: {int(rad_percentage)}%",
            True,
            rad_color
        )
        screen.blit(rad_text, (10, y_pos))
        y_pos += 30

        weather_text = self.small_font.render(
            f"Weather: {weather.current_weather}",
            True,
            COLOR_UI_TEXT
        )
        screen.blit(weather_text, (10, y_pos))
