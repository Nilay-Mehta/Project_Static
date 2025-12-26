import pygame
from entities.player import Player
from entities.mutant import Mutant
from entities.raider import Raider
from systems.camera import Camera
from systems.hazard_zone import HazardZone
from systems.weather import WeatherSystem
from enums import HazardType, GameState
from ui.hud import HUD


class GameScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.player = Player(400, 300)
        self.mutants = []
        self.raiders = []
        self.hazard_zones = []
        self.camera = Camera(game_manager.screen.get_width(),
                             game_manager.screen.get_height())
        self.weather = WeatherSystem()
        self.hud = HUD()

        self.mutants.append(Mutant(600, 200, "basic"))
        self.mutants.append(Mutant(800, 400, "fast"))
        self.raiders.append(Raider(500, 500))

        self.hazard_zones.append(HazardZone(700, 100, 200, 200,
                                            HazardType.RADIATION, 0.8))
        self.hazard_zones.append(HazardZone(200, 400, 150, 150,
                                            HazardType.TOXIC_GAS, 0.6))

    def on_enter(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game_manager.change_state(GameState.PAUSED)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        camera_offset = self.camera.offset

        self.player.handle_input(
            keys,
            mouse_buttons,
            mouse_pos,
            camera_offset
        )

        self.player.update(dt)

        self.weather.update(dt)
        weather_effects = self.weather.get_effects()

        if "radiation_rate" in weather_effects:
            self.player.add_radiation(weather_effects["radiation_rate"] * dt)

        for mutant in self.mutants[:]:
            mutant.update(dt, self.player)
            if not mutant.alive:
                self.mutants.remove(mutant)

        for raider in self.raiders[:]:
            raider.update(dt, self.player)
            if not raider.alive:
                self.raiders.remove(raider)

        for hazard in self.hazard_zones:
            hazard.affect_player(self.player, dt)

        self.camera.update(self.player)

        if not self.player.alive:
            self.game_manager.change_state(GameState.GAME_OVER)

    def render(self, screen):
        screen.fill((60, 55, 45))

        for hazard in self.hazard_zones:
            hazard.render(screen, self.camera.offset)

        self.player.render(screen, self.camera.offset)

        for mutant in self.mutants:
            mutant.render(screen, self.camera.offset)

        for raider in self.raiders:
            raider.render(screen, self.camera.offset)

        self.hud.render(screen, self.player, self.weather)