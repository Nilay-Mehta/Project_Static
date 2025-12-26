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
            if event.key == pygame.K_RETURN:
                self.game_manager.game_scene = GameScene(self.game_manager)
                self.game_manager.scenes[GameState.PLAYING] = self.game_manager.game_scene
                self.game_manager.change_state(GameState.PLAYING)
            elif event.key == pygame.K_q:
                self.game_manager.change_state(GameState.MENU)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill(COLOR_BG)

        title = self.font.render("YOU DIED", True, COLOR_UI_HEALTH)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 250))
        screen.blit(title, title_rect)

        restart_text = self.menu_font.render("ENTER - Restart", True, COLOR_UI_TEXT)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
        screen.blit(restart_text, restart_rect)

        quit_text = self.menu_font.render("Q - Main Menu", True, COLOR_UI_TEXT)
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, 400))
        screen.blit(quit_text, quit_rect)
