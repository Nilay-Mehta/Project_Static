import pygame
from pygame.math import Vector2
import random
from entities.entity import Entity
from constants import *


class Mutant(Entity):
    """
    Mutant enemy - all stats loaded from constants.py
    Types: basic, fast, tank
    """

    # Load configurations from constants
    MUTANT_CONFIGS = {
        "basic": {
            "max_health": MUTANT_BASIC_HEALTH,
            "speed": MUTANT_BASIC_SPEED,
            "damage": MUTANT_BASIC_DAMAGE,
            "color": MUTANT_BASIC_COLOR
        },
        "fast": {
            "max_health": MUTANT_FAST_HEALTH,
            "speed": MUTANT_FAST_SPEED,
            "damage": MUTANT_FAST_DAMAGE,
            "color": MUTANT_FAST_COLOR
        },
        "tank": {
            "max_health": MUTANT_TANK_HEALTH,
            "speed": MUTANT_TANK_SPEED,
            "damage": MUTANT_TANK_DAMAGE,
            "color": MUTANT_TANK_COLOR
        }
    }

    def __init__(self, x, y, mutant_type="basic"):
        """Create a mutant at position (x, y)."""
        if mutant_type not in self.MUTANT_CONFIGS:
            mutant_type = "basic"

        config = self.MUTANT_CONFIGS[mutant_type]

        super().__init__(x, y,
                         width=MUTANT_WIDTH,
                         height=MUTANT_HEIGHT,
                         max_health=config["max_health"])

        self.mutant_type = mutant_type
        self.speed = config["speed"]
        self.color = config["color"]
        self.damage = config["damage"]

        # Combat stats from constants
        self.attack_range = MUTANT_ATTACK_RANGE
        self.detection_range = MUTANT_DETECTION_RANGE
        self.attack_cooldown = 0
        self.attack_delay = MUTANT_ATTACK_DELAY

        # AI state
        self.wander_timer = 0
        self.wander_direction = Vector2(0, 0)
        self.target = None

    def update(self, dt, player):
        """Update mutant AI and position."""
        super().update(dt)

        self.attack_cooldown = max(0, self.attack_cooldown - dt)

        distance_to_player = self.pos.distance_to(player.pos)

        if distance_to_player < self.detection_range:
            # Chase player
            self.target = player

            direction = (player.pos - self.pos)
            if direction.length() > 0:
                direction = direction.normalize()
                self.velocity = direction * self.speed

            # Attack if in range
            if distance_to_player < self.attack_range and self.attack_cooldown <= 0:
                self.attack(player)
                self.attack_cooldown = self.attack_delay
        else:
            # Wander
            self.wander(dt)

    def wander(self, dt):
        """Random wandering behavior."""
        self.wander_timer -= dt

        if self.wander_timer <= 0:
            self.wander_direction = Vector2(
                random.uniform(-1, 1),
                random.uniform(-1, 1)
            )
            if self.wander_direction.length() > 0:
                self.wander_direction = self.wander_direction.normalize()

            self.wander_timer = random.uniform(2, 5)

        self.velocity = self.wander_direction * self.speed * MUTANT_WANDER_SPEED_MULTIPLIER

    def attack(self, player):
        """Attack the player."""
        player.take_damage(self.damage)

    def render(self, screen, camera_offset):
        """Render mutant to screen."""
        super().render(screen, camera_offset)
        self.render_health_bar(screen, camera_offset)

    def render_health_bar(self, screen, camera_offset):
        """Draw health bar above mutant."""
        bar_width = self.width
        bar_height = 4
        bar_x = self.rect.x - camera_offset[0]
        bar_y = self.rect.y - camera_offset[1] - 8

        # Background
        pygame.draw.rect(screen, (100, 0, 0),
                         (bar_x, bar_y, bar_width, bar_height))

        # Health
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, (0, 200, 0),
                         (bar_x, bar_y, int(bar_width * health_ratio), bar_height))
