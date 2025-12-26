import pygame
from enums import GameState
from scenes.game_scene import GameScene
from constants import *


class GameOverScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, UI_TITLE_FONT_SIZE)
        self.menu_font = pygame.font.Font(None, UI_FONT_SIZE)

    def on_enter(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == GAME_OVER_RESTART_KEY:   # ⬅ constant
                self.game_manager.game_scene = GameScene(self.game_manager)
                self.game_manager.scenes[GameState.PLAYING] = self.game_manager.game_scene
                self.game_manager.change_state(GameState.PLAYING)

            elif event.key == GAME_OVER_MENU_KEY:    # ⬅ constant
                self.game_manager.change_state(GameState.MENU)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(COLOR_BG)

        # -------------------------
        # Game Over Title
        # -------------------------
        title = self.font.render(
            GAME_OVER_TITLE_TEXT, True, COLOR_UI_HEALTH
        )
        title_rect = title.get_rect(
            center=(SCREEN_WIDTH // 2, GAME_OVER_TITLE_Y)
        )
        screen.blit(title, title_rect)

        # -------------------------
        # Restart prompt
        # -------------------------
        restart_text = self.menu_font.render(
            GAME_OVER_RESTART_TEXT, True, COLOR_UI_TEXT
        )
        restart_rect = restart_text.get_rect(
            center=(SCREEN_WIDTH // 2, GAME_OVER_RESTART_Y)
        )
        screen.blit(restart_text, restart_rect)

        # -------------------------
        # Quit to menu prompt
        # -------------------------
        quit_text = self.menu_font.render(
            GAME_OVER_MENU_TEXT, True, COLOR_UI_TEXT
        )
        quit_rect = quit_text.get_rect(
            center=(SCREEN_WIDTH // 2, GAME_OVER_MENU_Y)
        )
        screen.blit(quit_text, quit_rect)
