import pygame
from pygame.math import Vector2
from entities.entity import Entity
from enums import EntityType
from config import (PLAYER_SPEED, PLAYER_MAX_HEALTH, PLAYER_MAX_STAMINA,
                    PLAYER_MAX_RADIATION, RADIATION_DAMAGE_THRESHOLD)


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, EntityType.PLAYER)

        self.health = PLAYER_MAX_HEALTH
        self.max_health = PLAYER_MAX_HEALTH
        self.stamina = PLAYER_MAX_STAMINA
        self.max_stamina = PLAYER_MAX_STAMINA
        self.hunger = 100
        self.thirst = 100
        self.radiation = 0
        self.max_radiation = PLAYER_MAX_RADIATION

        self.speed = PLAYER_SPEED
        self.is_running = False

        self.inventory = []
        self.equipped_weapon = None
        self.has_gas_mask = False
        self.has_rad_suit = False

        self.ammo = {"pistol": 30, "rifle": 60, "shotgun": 20}

        self.radiation_resistance = 0
        self.cold_resistance = 0
        self.toxin_resistance = 0

    def handle_input(self, keys):
        self.velocity = Vector2(0, 0)

        if keys[pygame.K_w]:
            self.velocity.y = -1
        if keys[pygame.K_s]:
            self.velocity.y = 1
        if keys[pygame.K_a]:
            self.velocity.x = -1
        if keys[pygame.K_d]:
            self.velocity.x = 1

        if self.velocity.length() > 0:
            self.velocity = self.velocity.normalize()

        self.is_running = keys[pygame.K_LSHIFT] and self.stamina > 0
        speed_multiplier = 1.5 if self.is_running else 1.0
        self.velocity *= self.speed * speed_multiplier

    def update(self, dt):
        super().update(dt)

        if self.is_running:
            self.stamina = max(0, self.stamina - 30 * dt)
        else:
            self.stamina = min(self.max_stamina, self.stamina + 20 * dt)

        self.hunger = max(0, self.hunger - 5 * dt / 60)
        self.thirst = max(0, self.thirst - 8 * dt / 60)

        if self.hunger <= 0 or self.thirst <= 0:
            self.health -= 5 * dt

        if self.radiation > RADIATION_DAMAGE_THRESHOLD:
            radiation_damage = (self.radiation - RADIATION_DAMAGE_THRESHOLD) * 0.1
            self.health -= radiation_damage * dt

    def add_radiation(self, amount):
        actual_radiation = amount * (1 - self.radiation_resistance / 100)
        self.radiation = min(self.max_radiation, self.radiation + actual_radiation)

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def eat(self, hunger_restore):
        self.hunger = min(100, self.hunger + hunger_restore)

    def drink(self, thirst_restore):
        self.thirst = min(100, self.thirst + thirst_restore)

    def use_rad_away(self, amount):
        self.radiation = max(0, self.radiation - amount)

    def render(self, screen, camera_offset=(0, 0)):
        color = (0, 150, 255)
        pygame.draw.rect(screen, color,
                         (self.rect.x - camera_offset[0],
                          self.rect.y - camera_offset[1],
                          self.width, self.height))