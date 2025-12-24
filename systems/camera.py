from pygame.math import Vector2


class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.offset = Vector2(0, 0)

    def update(self, target):
        self.offset.x = target.pos.x - self.width // 2
        self.offset.y = target.pos.y - self.height // 2