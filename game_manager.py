import pygame
from enums import GameState
from scenes.game_scene import GameScene
from scenes.menu_scene import MenuScene
from scenes.pause_scene import PauseScene
from scenes.game_over_scene import GameOverScene
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


class GameManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Nuclear Wasteland")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.MENU

        self.game_scene = GameScene(self)
        self.scenes = {
            GameState.MENU: MenuScene(self),
            GameState.PLAYING: self.game_scene,
            GameState.PAUSED: PauseScene(self),
            GameState.GAME_OVER: GameOverScene(self)
        }
        self.current_scene = self.scenes[self.state]

    def change_state(self, new_state):
        self.state = new_state
        self.current_scene = self.scenes[new_state]
        self.current_scene.on_enter()

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                self.current_scene.handle_event(event)

            self.current_scene.update(dt)

            self.screen.fill((0, 0, 0))
            self.current_scene.render(self.screen)
            pygame.display.flip()