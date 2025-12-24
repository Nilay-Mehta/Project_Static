import pygame
from enums import GameState
from scenes.game_scene import GameScene


class GameOverScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 72)
        self.menu_font = pygame.font.Font(None, 36)

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
        screen.fill((20, 15, 15))

        title = self.font.render("YOU DIED", True, (255, 50, 50))
        title_rect = title.get_rect(center=(screen.get_width() // 2, 250))
        screen.blit(title, title_rect)

        restart_text = self.menu_font.render("ENTER - Restart", True, (200, 200, 200))
        restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, 350))
        screen.blit(restart_text, restart_rect)

        quit_text = self.menu_font.render("Q - Main Menu", True, (200, 200, 200))
        quit_rect = quit_text.get_rect(center=(screen.get_width() // 2, 400))
        screen.blit(quit_text, quit_rect)