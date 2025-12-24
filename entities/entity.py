import pygame
from pygame.math import Vector2


class Entity:
    def __init__(self, x, y, width, height, entity_type):
        self.pos = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.width = width
        self.height = height
        self.entity_type = entity_type
        self.rect = pygame.Rect(x, y, width, height)
        self.alive = True
        self.sprite = None
        self.health = 100
        self.max_health = 100

    def update(self, dt):
        self.pos += self.velocity * dt
        self.rect.x = int(self.pos.x)
        self.rect.y = int(self.pos.y)

    def render(self, screen, camera_offset=(0, 0)):
        if self.sprite:
            screen.blit(self.sprite, (self.rect.x - camera_offset[0],
                                      self.rect.y - camera_offset[1]))
        else:
            color = (255, 0, 0)
            pygame.draw.rect(screen, color,
                             (self.rect.x - camera_offset[0],
                              self.rect.y - camera_offset[1],
                              self.width, self.height), 2)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.alive = False