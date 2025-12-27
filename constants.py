"""
GAME CONSTANTS - ALL TWEAKABLE VALUES IN ONE PLACE
Change values here to balance the game!
"""

import pygame

# ═════════════════════════════════════════════════════════════════════════
# SCREEN & PERFORMANCE
# ═════════════════════════════════════════════════════════════════════════
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# ═════════════════════════════════════════════════════════════════════════
# HEALTH SYSTEM (INTEGER BASED)
# ═════════════════════════════════════════════════════════════════════════
# Core conversion: 1 heart = 2 HP
HP_PER_HEART = 2
HALF_HEART = 1
FULL_HEART = 2

# ═════════════════════════════════════════════════════════════════════════
# PLAYER SETTINGS
# ═════════════════════════════════════════════════════════════════════════
PLAYER_START_HEARTS = 4
PLAYER_MAX_HEALTH = PLAYER_START_HEARTS * HP_PER_HEART
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 32
PLAYER_SPEED = 200
PLAYER_COLOR = (0, 150, 255)

# Player shooting
PLAYER_SHOOT_DELAY = 0.3
PLAYER_BULLET_SPEED = 500
PLAYER_BULLET_DAMAGE = FULL_HEART
PLAYER_BULLET_LIFETIME = 2.0
PLAYER_BULLET_SIZE = 8
PLAYER_BULLET_COLOR = (255, 255, 0)

# Player radiation
PLAYER_MAX_RADIATION = 100
PLAYER_RADIATION_THRESHOLD = 50
PLAYER_RADIATION_DAMAGE = HALF_HEART
PLAYER_RADIATION_DAMAGE_INTERVAL = 2.5

# ═════════════════════════════════════════════════════════════════════════
# MUTANT SETTINGS
# ═════════════════════════════════════════════════════════════════════════
MUTANT_WIDTH = 40
MUTANT_HEIGHT = 40
MUTANT_DETECTION_RANGE = 300
MUTANT_ATTACK_RANGE = 45
MUTANT_ATTACK_DELAY = 1.5
MUTANT_WANDER_SPEED_MULTIPLIER = 0.3

# Basic Mutant
MUTANT_BASIC_HEALTH = 4
MUTANT_BASIC_SPEED = 80
MUTANT_BASIC_DAMAGE = HALF_HEART
MUTANT_BASIC_COLOR = (150, 255, 150)

# Fast Mutant
MUTANT_FAST_HEALTH = 3
MUTANT_FAST_SPEED = 150
MUTANT_FAST_DAMAGE = HALF_HEART
MUTANT_FAST_COLOR = (255, 200, 100)

# Tank Mutant
MUTANT_TANK_HEALTH = 10
MUTANT_TANK_SPEED = 50
MUTANT_TANK_DAMAGE = FULL_HEART
MUTANT_TANK_COLOR = (200, 100, 100)

# ═════════════════════════════════════════════════════════════════════════
# RAIDER SETTINGS
# ═════════════════════════════════════════════════════════════════════════
RAIDER_WIDTH = 32
RAIDER_HEIGHT = 32
RAIDER_HEALTH = 6
RAIDER_SPEED = 100
RAIDER_DAMAGE = HALF_HEART
RAIDER_COLOR = (200, 50, 50)

RAIDER_DETECTION_RANGE = 350
RAIDER_WEAPON_RANGE = 300
RAIDER_OPTIMAL_DISTANCE = 200
RAIDER_DISTANCE_TOLERANCE = 50
RAIDER_SHOOT_DELAY = 2.0

RAIDER_BULLET_SPEED = 400
RAIDER_BULLET_SIZE = 6
RAIDER_BULLET_COLOR = (255, 100, 100)
RAIDER_BULLET_LIFETIME = 1.5

# ═════════════════════════════════════════════════════════════════════════
# HAZARD ZONES
# ═════════════════════════════════════════════════════════════════════════
RADIATION_ZONE_DAMAGE_RATE = 20
RADIATION_ZONE_COLOR = (0, 255, 0)
RADIATION_ZONE_ALPHA = 50

# ═════════════════════════════════════════════════════════════════════════
# GAME BALANCE / SPAWNING
# ═════════════════════════════════════════════════════════════════════════
MUTANT_SPAWN_INITIAL_INTERVAL = 5.0
MUTANT_SPAWN_MIN_INTERVAL = 3.0
MUTANT_SPAWN_DECREASE_RATE = 0.1

# ═════════════════════════════════════════════════════════════════════════
# COLORS (UI & VISUALS)
# ═════════════════════════════════════════════════════════════════════════
COLOR_BG = (40, 35, 30)
COLOR_GROUND = (60, 55, 45)
COLOR_UI_TEXT = (255, 255, 255)
COLOR_UI_HEALTH = (255, 50, 50)
COLOR_UI_RADIATION_LOW = (100, 255, 100)
COLOR_UI_RADIATION_MED = (255, 200, 0)
COLOR_UI_RADIATION_HIGH = (255, 50, 50)

# ═════════════════════════════════════════════════════════════════════════
# UI FONT SIZES
# ═════════════════════════════════════════════════════════════════════════
UI_FONT_SIZE = 24
UI_TITLE_FONT_SIZE = 72

# ═════════════════════════════════════════════════════════════════════════
# HUD LAYOUT
# ═════════════════════════════════════════════════════════════════════════
HUD_PADDING_X = 10
HUD_PADDING_Y = 10
HUD_LINE_HEIGHT = 15  # Exact height of text
HUD_LINE_SPACING = 5  # Spacing between lines
HUD_SECTION_SPACING = 30
BAR_HEIGHT = 20  # Height of health, stamina bar
BAR_SPACING = 5  # Vertical space between bars

# ═════════════════════════════════════════════════════════════════════════
# HEALTH BAR UI
# ═════════════════════════════════════════════════════════════════════════
HEALTH_BAR_WIDTH = 200
HEALTH_BAR_HEIGHT = 20
HEALTH_BAR_X = HUD_PADDING_X
HEALTH_BAR_Y_OFFSET = 8
HEALTH_BAR_BORDER_WIDTH = 2

# ═════════════════════════════════════════════════════════════════════════
# HUD / RADIATION UI THRESHOLDS
# ═════════════════════════════════════════════════════════════════════════
RADIATION_UI_MED_THRESHOLD = 50
RADIATION_UI_HIGH_THRESHOLD = 80

# ═════════════════════════════════════════════════════════════════════════
# MENU SCENE
# ═════════════════════════════════════════════════════════════════════════
MENU_START_KEY = pygame.K_RETURN

MENU_TITLE_TEXT = "NUCLEAR WASTELAND"
MENU_SUBTITLE_TEXT = "Post-Apocalyptic Survival"
MENU_START_TEXT = "Press ENTER to Start"

MENU_TITLE_Y = 200
MENU_SUBTITLE_Y = 280
MENU_START_Y = 400

# ═════════════════════════════════════════════════════════════════════════
# GAME OVER SCENE
# ═════════════════════════════════════════════════════════════════════════
GAME_OVER_RESTART_KEY = pygame.K_RETURN
GAME_OVER_MENU_KEY = pygame.K_q

GAME_OVER_TITLE_TEXT = "YOU DIED"
GAME_OVER_RESTART_TEXT = "ENTER - Restart"
GAME_OVER_MENU_TEXT = "Q - Main Menu"

GAME_OVER_TITLE_Y = 250
GAME_OVER_RESTART_Y = 350
GAME_OVER_MENU_Y = 400

# ═════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═════════════════════════════════════════════════════════════════════════
def hearts_to_hp(hearts):
    """Convert hearts to HP"""
    return int(hearts * HP_PER_HEART)

def hp_to_hearts(hp):
    """Convert HP to hearts (full and half)"""
    full_hearts = hp // HP_PER_HEART
    half_hearts = hp % HP_PER_HEART
    return full_hearts, half_hearts
