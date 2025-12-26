import pygame
from pygame.math import Vector2
from constants import HP_PER_HEART


class Entity:
    """
    Base class for all moving entities in the game.

    HEALTH SYSTEM (INTEGER ONLY):
        Uses constants.HP_PER_HEART for conversions
        Default: 1 heart = 2 HP

    Attributes:
        pos (Vector2): Position in world space
        velocity (Vector2): Movement vector
        width, height (int): Entity dimensions
        rect (pygame.Rect): Collision rectangle
        alive (bool): Whether entity is still active
        health (int): Current health points (INTEGER)
        max_health (int): Maximum health points (INTEGER)
    """

    def __init__(self, x, y, width, height, max_health=8):
        """
        Initialize entity.

        Args:
            x, y: Starting position
            width, height: Entity size in pixels
            max_health: Maximum HP in integer
        """
        self.pos = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.alive = True
        self.max_health = int(max_health)
        self.health = int(max_health)

        # Visual properties
        self.sprite = None
        self.color = (255, 255, 255)

    def update(self, dt):
        """
        Update entity position based on velocity.

        Args:
            dt: Delta time in seconds
        """
        self.pos += self.velocity * dt
        self.rect.x = int(self.pos.x)
        self.rect.y = int(self.pos.y)

    def take_damage(self, amount):
        """
        Apply damage to entity (INTEGER ONLY).

        Args:
            amount (int): Damage in HP
        """
        amount = int(amount)
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.alive = False

    def heal(self, amount):
        """
        Restore health to entity (INTEGER ONLY).

        Args:
            amount (int): HP to restore
        """
        amount = int(amount)
        self.health = min(self.max_health, self.health + amount)

    def get_hearts(self):
        """
        Get current health in hearts.

        Returns:
            tuple: (full_hearts, half_hearts)
        """
        full_hearts = self.health // HP_PER_HEART
        half_hearts = self.health % HP_PER_HEART
        return full_hearts, half_hearts

    def get_max_hearts(self):
        """
        Get max health as hearts.

        Returns:
            int: Max hearts
        """
        return self.max_health // HP_PER_HEART

    def render(self, screen, camera_offset):
        """
        Render entity to screen.

        Args:
            screen: pygame Surface
            camera_offset: (x, y) tuple
        """
        if self.sprite:
            screen.blit(self.sprite,
                       (self.rect.x - camera_offset[0],
                        self.rect.y - camera_offset[1]))
        else:
            pygame.draw.rect(screen, self.color,
                           (self.rect.x - camera_offset[0],
                            self.rect.y - camera_offset[1],
                            self.width, self.height))