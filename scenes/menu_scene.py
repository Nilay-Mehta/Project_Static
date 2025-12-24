import pygame
from enums import GameState
from config import COLOR_BG


class MenuScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 48)
        self.title_font = pygame.font.Font(None, 72)

    def on_enter(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game_manager.change_state(GameState.PLAYING)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(COLOR_BG)

        title = self.title_font.render("NUCLEAR WASTELAND", True, (255, 140, 0))
        title_rect = title.get_rect(center=(screen.get_width() // 2, 200))
        screen.blit(title, title_rect)

        subtitle = self.font.render("Post-Apocalyptic Survival", True, (200, 200, 200))
        subtitle_rect = subtitle.get_rect(center=(screen.get_width() // 2, 280))
        screen.blit(subtitle, subtitle_rect)

        start_text = self.font.render("Press ENTER to Start", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(screen.get_width() // 2, 400))
        screen.blit(start_text, start_rect)