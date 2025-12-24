import pygame
from enums import GameState


class PauseScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 72)
        self.menu_font = pygame.font.Font(None, 36)

    def on_enter(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game_manager.change_state(GameState.PLAYING)
            elif event.key == pygame.K_q:
                self.game_manager.change_state(GameState.MENU)

    def update(self, dt):
        pass

    def render(self, screen):
        self.game_manager.game_scene.render(screen)

        overlay = pygame.Surface(screen.get_size())
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        title = self.font.render("PAUSED", True, (255, 255, 255))
        title_rect = title.get_rect(center=(screen.get_width() // 2, 250))
        screen.blit(title, title_rect)

        resume_text = self.menu_font.render("ESC - Resume", True, (200, 200, 200))
        resume_rect = resume_text.get_rect(center=(screen.get_width() // 2, 350))
        screen.blit(resume_text, resume_rect)

        quit_text = self.menu_font.render("Q - Quit to Menu", True, (200, 200, 200))
        quit_rect = quit_text.get_rect(center=(screen.get_width() // 2, 400))
        screen.blit(quit_text, quit_rect)