import random
from enums import HazardType


class WeatherSystem:
    def __init__(self):
        self.current_weather = "clear"
        self.weather_timer = 0
        self.weather_duration = 60

        self.weathers = ["clear", "dust_storm", "radiation_storm", "cold_front"]

    def update(self, dt):
        self.weather_timer += dt

        if self.weather_timer >= self.weather_duration:
            self.change_weather()
            self.weather_timer = 0

    def change_weather(self):
        self.current_weather = random.choice(self.weathers)
        self.weather_duration = random.uniform(45, 120)

    def get_effects(self):
        if self.current_weather == "dust_storm":
            return {"visibility": 0.4, "movement_penalty": 0.8}
        elif self.current_weather == "radiation_storm":
            return {"radiation_rate": 15, "visibility": 0.6}
        elif self.current_weather == "cold_front":
            return {"cold_damage": True, "movement_penalty": 0.9}
        return {}