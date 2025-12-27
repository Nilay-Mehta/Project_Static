import pygame
from constants import *
from ui.health_bar import HealthBar


class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, UI_FONT_SIZE)
        self.small_font = pygame.font.Font(None, UI_FONT_SIZE - 4)
        self.health_bar = HealthBar()

    def render(self, screen, player, weather):
        y_pos = HUD_PADDING_Y

        # -------------------------
        # Health
        # -------------------------
        health_text = self.font.render(
            f"Health: {int(player.health)}/{PLAYER_MAX_HEALTH}",
            True,
            COLOR_UI_HEALTH
        )
        screen.blit(health_text, (HUD_PADDING_X, y_pos))
        y_pos += HUD_LINE_HEIGHT + BAR_SPACING

        self.health_bar.render(screen, current_health=player.health, x=HUD_PADDING_X, y=y_pos)
        y_pos += BAR_HEIGHT + BAR_SPACING

        # -------------------------
        # Stamina
        # -------------------------
        stamina_text = self.font.render(
            f"Stamina: {int(player.stamina)}",
            True,
            COLOR_UI_TEXT
        )
        screen.blit(stamina_text, (HUD_PADDING_X, y_pos))
        y_pos += HUD_LINE_HEIGHT + HUD_LINE_SPACING

        # -------------------------
        # Radiation
        # -------------------------
        rad_percentage = (player.radiation / PLAYER_MAX_RADIATION) * 100

        if rad_percentage >= RADIATION_UI_HIGH_THRESHOLD:
            rad_color = COLOR_UI_RADIATION_HIGH
        elif rad_percentage >= RADIATION_UI_MED_THRESHOLD:
            rad_color = COLOR_UI_RADIATION_MED
        else:
            rad_color = COLOR_UI_RADIATION_LOW

        rad_text = self.font.render(
            f"Radiation: {int(rad_percentage)}%",
            True,
            rad_color
        )
        screen.blit(rad_text, (HUD_PADDING_X, y_pos))
        y_pos += HUD_SECTION_SPACING

        # -------------------------
        # Weather
        # -------------------------
        weather_text = self.small_font.render(
            f"Weather: {weather.current_weather}",
            True,
            COLOR_UI_TEXT
        )
        screen.blit(weather_text, (HUD_PADDING_X, y_pos))
