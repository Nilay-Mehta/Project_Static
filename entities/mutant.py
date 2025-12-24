import pygame
from pygame.math import Vector2
import random
from entities.entity import Entity
from enums import EntityType


class Mutant(Entity):
    def __init__(self, x, y, mutant_type="basic"):
        super().__init__(x, y, 40, 40, EntityType.MUTANT)

        self.mutant_type = mutant_type

        if mutant_type == "basic":
            self.health = 60
            self.max_health = 60
            self.speed = 80
            self.damage = 15
        elif mutant_type == "fast":
            self.health = 40
            self.max_health = 40
            self.speed = 150
            self.damage = 10
        elif mutant_type == "tank":
            self.health = 150
            self.max_health = 150
            self.speed = 40
            self.damage = 25

        self.attack_range = 45
        self.detection_range = 250
        self.attack_cooldown = 0
        self.attack_delay = 1.5

        self.target = None
        self.wander_timer = 0
        self.wander_direction = Vector2(0, 0)
        self.aggro = False

    def update(self, dt, player):
        super().update(dt)

        self.attack_cooldown = max(0, self.attack_cooldown - dt)

        distance_to_player = self.pos.distance_to(player.pos)

        if distance_to_player < self.detection_range or self.aggro:
            self.aggro = True
            self.target = player
            direction = (player.pos - self.pos)
            if direction.length() > 0:
                direction = direction.normalize()
                self.velocity = direction * self.speed

            if distance_to_player < self.attack_range and self.attack_cooldown <= 0:
                player.take_damage(self.damage)
                self.attack_cooldown = self.attack_delay
        else:
            self.wander_timer -= dt
            if self.wander_timer <= 0:
                self.wander_direction = Vector2(random.uniform(-1, 1),
                                                random.uniform(-1, 1))
                if self.wander_direction.length() > 0:
                    self.wander_direction = self.wander_direction.normalize()
                self.wander_timer = random.uniform(2, 5)

            self.velocity = self.wander_direction * self.speed * 0.3

    def render(self, screen, camera_offset=(0, 0)):
        color = (150, 255, 150) if self.mutant_type == "basic" else (255, 200, 100)
        pygame.draw.rect(screen, color,
                         (self.rect.x - camera_offset[0],
                          self.rect.y - camera_offset[1],
                          self.width, self.height))
