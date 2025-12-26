import pygame
from pygame.math import Vector2
from entities.entity import Entity
from constants import *


class Raider(Entity):
    """
    Raider enemy - human scavenger with gun.

    Behavior:
        - Detects player at long range
        - Tries to maintain optimal distance (kiting)
        - Backs away if player gets too close
        - Strafes when at optimal distance
        - Shoots at player when in range
    """

    def __init__(self, x, y):
        """Create a raider at position (x, y)."""
        super().__init__(x, y,
                         width=RAIDER_WIDTH,
                         height=RAIDER_HEIGHT,
                         max_health=RAIDER_HEALTH)

        self.speed = RAIDER_SPEED
        self.color = RAIDER_COLOR
        self.damage = RAIDER_DAMAGE

        # Combat stats from constants
        self.weapon_range = RAIDER_WEAPON_RANGE
        self.optimal_distance = RAIDER_OPTIMAL_DISTANCE
        self.distance_tolerance = RAIDER_DISTANCE_TOLERANCE
        self.detection_range = RAIDER_DETECTION_RANGE

        self.shoot_cooldown = 0
        self.shoot_delay = RAIDER_SHOOT_DELAY

        # AI state
        self.target = None
        self.bullets = []
        self.strafe_direction = 1  # 1 or -1 for left/right strafing
        self.strafe_timer = 0

    def update(self, dt, player):
        """
        Update raider AI and position.

        Args:
            dt: Delta time in seconds
            player: Player entity to track and shoot
        """
        super().update(dt)

        self.shoot_cooldown = max(0, self.shoot_cooldown - dt)
        self.strafe_timer += dt

        # Change strafe direction periodically
        if self.strafe_timer > 2.0:
            self.strafe_direction *= -1
            self.strafe_timer = 0

        distance_to_player = self.pos.distance_to(player.pos)

        if distance_to_player < self.detection_range:
            self.target = player

            # Calculate direction to player
            direction = (player.pos - self.pos)
            if direction.length() > 0:
                direction = direction.normalize()

                # KITING AI: Maintain optimal distance
                if distance_to_player < self.optimal_distance - self.distance_tolerance:
                    # TOO CLOSE: Back away from player
                    self.velocity = -direction * self.speed

                elif distance_to_player > self.optimal_distance + self.distance_tolerance:
                    # TOO FAR: Move closer to player
                    self.velocity = direction * self.speed

                else:
                    # OPTIMAL RANGE: Strafe to avoid being easy target
                    perpendicular = Vector2(-direction.y, direction.x)
                    self.velocity = perpendicular * self.speed * 0.5 * self.strafe_direction

                # Shoot if in range and cooldown ready
                if distance_to_player < self.weapon_range and self.shoot_cooldown <= 0:
                    self.shoot(player)
                    self.shoot_cooldown = self.shoot_delay
        else:
            # No target, stand still
            self.velocity = Vector2(0, 0)

        # Update bullets
        for bullet in self.bullets[:]:
            bullet.update(dt)
            if not bullet.alive:
                self.bullets.remove(bullet)

    def shoot(self, player):
        """
        Fire a bullet at the player.

        Args:
            player: Player entity to shoot at
        """
        # Calculate direction to player
        direction = (player.pos - self.pos)
        if direction.length() > 0:
            direction = direction.normalize()

        # Create bullet at raider center
        bullet = RaiderBullet(
            self.pos.x + self.width // 2,
            self.pos.y + self.height // 2,
            direction
        )
        self.bullets.append(bullet)

    def render(self, screen, camera_offset):
        """
        Render raider and bullets to screen.

        Args:
            screen: pygame Surface
            camera_offset: (x, y) camera position
        """
        # Draw raider
        super().render(screen, camera_offset)

        # Draw health bar
        self.render_health_bar(screen, camera_offset)

        # Draw bullets
        for bullet in self.bullets:
            bullet.render(screen, camera_offset)

    def render_health_bar(self, screen, camera_offset):
        """Draw health bar above raider."""
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


class RaiderBullet:
    """
    Projectile fired by raider.

    Attributes:
        pos (Vector2): Current position
        direction (Vector2): Normalized movement direction
        speed (float): Pixels per second
        damage (int): Damage dealt on hit (INTEGER)
        alive (bool): Whether bullet is still active
    """

    def __init__(self, x, y, direction):
        """
        Create a raider bullet.

        Args:
            x, y: Starting position
            direction: Normalized Vector2 for movement direction
        """
        self.pos = Vector2(x, y)
        self.direction = direction
        self.speed = RAIDER_BULLET_SPEED
        self.damage = RAIDER_DAMAGE
        self.alive = True
        self.lifetime = RAIDER_BULLET_LIFETIME
        self.age = 0
        self.rect = pygame.Rect(int(x), int(y),
                                RAIDER_BULLET_SIZE, RAIDER_BULLET_SIZE)

        # Visual
        self.radius = RAIDER_BULLET_SIZE // 2
        self.color = RAIDER_BULLET_COLOR

    def update(self, dt):
        """
        Update bullet position and lifetime.

        Args:
            dt: Delta time in seconds
        """
        # Move bullet
        self.pos += self.direction * self.speed * dt

        # Update collision rect
        self.rect.x = int(self.pos.x - self.radius)
        self.rect.y = int(self.pos.y - self.radius)

        # Track lifetime
        self.age += dt
        if self.age >= self.lifetime:
            self.alive = False

    def render(self, screen, camera_offset):
        """
        Render bullet as a circle.

        Args:
            screen: pygame Surface
            camera_offset: (x, y) camera position
        """
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.pos.x - camera_offset[0]),
             int(self.pos.y - camera_offset[1])),
            self.radius
        )
