import pygame


class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 20)

    def render(self, screen, player, weather):
        y_pos = 10

        health_text = self.font.render(
            f"Health: {int(player.health)}/{player.max_health}",
            True, (255, 50, 50))
        screen.blit(health_text, (10, y_pos))
        y_pos += 25

        stamina_text = self.font.render(
            f"Stamina: {int(player.stamina)}",
            True, (255, 255, 100))
        screen.blit(stamina_text, (10, y_pos))
        y_pos += 25

        rad_percentage = (player.radiation / player.max_radiation) * 100
        rad_color = (100, 255, 100)
        if rad_percentage > 50:
            rad_color = (255, 200, 0)
        if rad_percentage > 80:
            rad_color = (255, 50, 50)

        rad_text = self.font.render(
            f"Radiation: {int(rad_percentage)}%", True, rad_color)
        screen.blit(rad_text, (10, y_pos))
        y_pos += 30

        weather_text = self.small_font.render(
            f"Weather: {weather.current_weather}",
            True, (200, 200, 200))
        screen.blit(weather_text, (10, y_pos))