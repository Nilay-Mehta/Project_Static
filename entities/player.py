import pygame
from pygame.math import Vector2
from entities.entity import Entity
from constants import *


class Player(Entity):
    """
    Player character with shooting and heart-based health.
    All values loaded from constants.py
    """

    def __init__(self, x, y):
        """Initialize player at position (x, y)."""
        super().__init__(x, y,
                        width=PLAYER_WIDTH,
                        height=PLAYER_HEIGHT,
                        max_health=PLAYER_MAX_HEALTH)

        # Stamina system (required by HUD)
        self.stamina = 100
        self.max_stamina = 100

        # Movement
        self.speed = PLAYER_SPEED
        self.color = PLAYER_COLOR

        # Radiation system
        self.radiation = 0
        self.max_radiation = PLAYER_MAX_RADIATION
        self.radiation_damage_threshold = PLAYER_RADIATION_THRESHOLD
        self.radiation_damage_timer = 0
        self.radiation_damage_interval = PLAYER_RADIATION_DAMAGE_INTERVAL

        # Shooting
        self.shoot_cooldown = 0
        self.shoot_delay = PLAYER_SHOOT_DELAY
        self.bullets = []

    def handle_input(self, keys, mouse_buttons, mouse_pos, camera_offset):
        """Handle player input."""
        self.velocity = Vector2(0, 0)

        # WASD movement
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

        self.velocity *= self.speed

        # Shooting
        if mouse_buttons[0] and self.shoot_cooldown <= 0:
            self.shoot(mouse_pos, camera_offset)
            self.shoot_cooldown = self.shoot_delay

    def shoot(self, mouse_pos, camera_offset):
        """Create a bullet towards mouse position."""
        target_x = mouse_pos[0] + camera_offset[0]
        target_y = mouse_pos[1] + camera_offset[1]

        direction = Vector2(target_x - self.pos.x, target_y - self.pos.y)
        if direction.length() > 0:
            direction = direction.normalize()

        bullet = Bullet(
            self.pos.x + self.width // 2,
            self.pos.y + self.height // 2,
            direction
        )
        self.bullets.append(bullet)

    def update(self, dt):
        """Update player state."""
        super().update(dt)

        self.shoot_cooldown = max(0, self.shoot_cooldown - dt)

        # Radiation damage
        if self.radiation > self.radiation_damage_threshold:
            self.radiation_damage_timer += dt

            if self.radiation_damage_timer >= self.radiation_damage_interval:
                self.take_damage(PLAYER_RADIATION_DAMAGE)
                self.radiation_damage_timer = 0

        # Update bullets
        for bullet in self.bullets[:]:
            bullet.update(dt)
            if not bullet.alive:
                self.bullets.remove(bullet)

    def add_radiation(self, amount):
        """Add radiation exposure."""
        self.radiation = min(self.max_radiation, int(self.radiation + amount))

    def render(self, screen, camera_offset):
        """Render player and bullets."""
        super().render(screen, camera_offset)

        for bullet in self.bullets:
            bullet.render(screen, camera_offset)


class Bullet:
    """Projectile fired by player - uses constants.py"""

    def __init__(self, x, y, direction):
        """Create a bullet."""
        self.pos = Vector2(x, y)
        self.direction = direction
        self.speed = PLAYER_BULLET_SPEED
        self.damage = PLAYER_BULLET_DAMAGE
        self.alive = True
        self.lifetime = PLAYER_BULLET_LIFETIME
        self.age = 0
        self.rect = pygame.Rect(int(x), int(y),
                               PLAYER_BULLET_SIZE, PLAYER_BULLET_SIZE)

        # Visual
        self.radius = PLAYER_BULLET_SIZE // 2
        self.color = PLAYER_BULLET_COLOR

    def update(self, dt):
        """Update bullet position and lifetime."""
        self.pos += self.direction * self.speed * dt

        self.rect.x = int(self.pos.x - self.radius)
        self.rect.y = int(self.pos.y - self.radius)

        self.age += dt
        if self.age >= self.lifetime:
            self.alive = False

    def render(self, screen, camera_offset):
        """Render bullet as a circle."""
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.pos.x - camera_offset[0]),
             int(self.pos.y - camera_offset[1])),
            self.radius
        )
