import pygame
from enums import HazardType
from config import COLOR_RADIATION, COLOR_TOXIC, COLOR_COLD


class HazardZone:
    def __init__(self, x, y, width, height, hazard_type, intensity=1.0):
        self.rect = pygame.Rect(x, y, width, height)
        self.hazard_type = hazard_type
        self.intensity = intensity
        self.active = True

    def affect_player(self, player, dt):
        if not self.active or not self.rect.colliderect(player.rect):
            return

        if self.hazard_type == HazardType.RADIATION:
            base_radiation = 20 * self.intensity * dt
            player.add_radiation(base_radiation)

        elif self.hazard_type == HazardType.TOXIC_GAS:
            if not player.has_gas_mask:
                player.take_damage(10 * self.intensity * dt)

        elif self.hazard_type == HazardType.EXTREME_COLD:
            if player.cold_resistance < 50:
                player.take_damage(5 * self.intensity * dt)

    def render(self, screen, camera_offset=(0, 0)):
        color = COLOR_RADIATION
        if self.hazard_type == HazardType.TOXIC_GAS:
            color = COLOR_TOXIC
        elif self.hazard_type == HazardType.EXTREME_COLD:
            color = COLOR_COLD

        surface = pygame.Surface((self.rect.width, self.rect.height))
        surface.set_alpha(50)
        surface.fill(color[:3])
        screen.blit(surface, (self.rect.x - camera_offset[0],
                              self.rect.y - camera_offset[1]))