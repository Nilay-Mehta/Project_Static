import pygame
from pygame.math import Vector2
import random
from entities.entity import Entity
from enums import EntityType


class Raider(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 32, 32, EntityType.RAIDER)

        self.health = 80
        self.max_health = 80
        self.speed = 100
        self.damage = 20

        self.weapon_range = 300
        self.optimal_distance = 200
        self.detection_range = 350

        self.shoot_cooldown = 0
        self.shoot_delay = 2.0

        self.target = None

    def update(self, dt, player):
        super().update(dt)

        self.shoot_cooldown = max(0, self.shoot_cooldown - dt)

        distance_to_player = self.pos.distance_to(player.pos)

        if distance_to_player < self.detection_range:
            self.target = player
            direction = (player.pos - self.pos)

            if direction.length() > 0:
                direction = direction.normalize()

                if distance_to_player < self.optimal_distance - 50:
                    self.velocity = -direction * self.speed
                elif distance_to_player > self.optimal_distance + 50:
                    self.velocity = direction * self.speed
                else:
                    perpendicular = Vector2(-direction.y, direction.x)
                    self.velocity = perpendicular * self.speed * 0.5

                if distance_to_player < self.weapon_range and self.shoot_cooldown <= 0:
                    self.shoot(player)
                    self.shoot_cooldown = self.shoot_delay
        else:
            self.velocity = Vector2(0, 0)

    def shoot(self, player):
        player.take_damage(self.damage)

    def render(self, screen, camera_offset=(0, 0)):
        color = (200, 50, 50)
        pygame.draw.rect(screen, color,
                         (self.rect.x - camera_offset[0],
                          self.rect.y - camera_offset[1],
                          self.width, self.height))