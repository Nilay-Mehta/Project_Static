import pygame
from enums import GameState
from constants import *


class MenuScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, UI_FONT_SIZE)
        self.title_font = pygame.font.Font(None, UI_TITLE_FONT_SIZE)

    def on_enter(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == MENU_START_KEY:  # ⬅ constant
                self.game_manager.change_state(GameState.PLAYING)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(COLOR_BG)

        # -------------------------
        # Title
        # -------------------------
        title = self.title_font.render(
            MENU_TITLE_TEXT, True, COLOR_UI_HEALTH
        )
        title_rect = title.get_rect(
            center=(SCREEN_WIDTH // 2, MENU_TITLE_Y)
        )
        screen.blit(title, title_rect)

        # -------------------------
        # Subtitle
        # -------------------------
        subtitle = self.font.render(
            MENU_SUBTITLE_TEXT, True, COLOR_UI_TEXT
        )
        subtitle_rect = subtitle.get_rect(
            center=(SCREEN_WIDTH // 2, MENU_SUBTITLE_Y)
        )
        screen.blit(subtitle, subtitle_rect)

        # -------------------------
        # Start prompt
        # -------------------------
        start_text = self.font.render(
            MENU_START_TEXT, True, COLOR_UI_TEXT
        )
        start_rect = start_text.get_rect(
            center=(SCREEN_WIDTH // 2, MENU_START_Y)
        )
        screen.blit(start_text, start_rect)
