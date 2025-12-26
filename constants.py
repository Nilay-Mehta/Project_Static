"""
GAME CONSTANTS - ALL TWEAKABLE VALUES IN ONE PLACE
Change values here to balance the game!
"""

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
PLAYER_START_HEARTS = 4  # Starting hearts
PLAYER_MAX_HEALTH = PLAYER_START_HEARTS * HP_PER_HEART  # 8 HP
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 32
PLAYER_SPEED = 200  # Pixels per second
PLAYER_COLOR = (0, 150, 255)  # Blue

# Player shooting
PLAYER_SHOOT_DELAY = 0.3  # Seconds between shots
PLAYER_BULLET_SPEED = 500
PLAYER_BULLET_DAMAGE = FULL_HEART  # 1 heart per bullet
PLAYER_BULLET_LIFETIME = 2.0  # Seconds
PLAYER_BULLET_SIZE = 8
PLAYER_BULLET_COLOR = (255, 255, 0)  # Yellow

# Player radiation
PLAYER_MAX_RADIATION = 100
PLAYER_RADIATION_THRESHOLD = 50  # Start taking damage above this
PLAYER_RADIATION_DAMAGE = HALF_HEART  # Damage per interval
PLAYER_RADIATION_DAMAGE_INTERVAL = 2.5  # Seconds between damage ticks

# ═════════════════════════════════════════════════════════════════════════
# MUTANT SETTINGS (ALL TYPES)
# ═════════════════════════════════════════════════════════════════════════
MUTANT_WIDTH = 40
MUTANT_HEIGHT = 40
MUTANT_DETECTION_RANGE = 300  # Pixels - how far they see player
MUTANT_ATTACK_RANGE = 45  # Pixels - melee range
MUTANT_ATTACK_DELAY = 1.5  # Seconds between attacks
MUTANT_WANDER_SPEED_MULTIPLIER = 0.3  # 30% speed when wandering

# Basic Mutant (balanced)
MUTANT_BASIC_HEALTH = 4  # 2 hearts
MUTANT_BASIC_SPEED = 80
MUTANT_BASIC_DAMAGE = HALF_HEART
MUTANT_BASIC_COLOR = (150, 255, 150)  # Light green

# Fast Mutant (weak but quick)
MUTANT_FAST_HEALTH = 3  # 1.5 hearts
MUTANT_FAST_SPEED = 150
MUTANT_FAST_DAMAGE = HALF_HEART
MUTANT_FAST_COLOR = (255, 200, 100)  # Orange

# Tank Mutant (slow but tough)
MUTANT_TANK_HEALTH = 10  # 5 hearts
MUTANT_TANK_SPEED = 50
MUTANT_TANK_DAMAGE = FULL_HEART
MUTANT_TANK_COLOR = (200, 100, 100)  # Dark red

# ═════════════════════════════════════════════════════════════════════════
# RAIDER SETTINGS
# ═════════════════════════════════════════════════════════════════════════
RAIDER_WIDTH = 32
RAIDER_HEIGHT = 32
RAIDER_HEALTH = 6  # 3 hearts
RAIDER_SPEED = 100
RAIDER_DAMAGE = HALF_HEART  # Half heart per shot
RAIDER_COLOR = (200, 50, 50)  # Red

# Raider AI behavior
RAIDER_DETECTION_RANGE = 350  # How far they see player
RAIDER_WEAPON_RANGE = 300  # How far they can shoot
RAIDER_OPTIMAL_DISTANCE = 200  # Distance they try to maintain (kiting)
RAIDER_DISTANCE_TOLERANCE = 50  # How close to optimal before adjusting
RAIDER_SHOOT_DELAY = 2.0  # Seconds between shots

# Raider projectile
RAIDER_BULLET_SPEED = 400
RAIDER_BULLET_SIZE = 6
RAIDER_BULLET_COLOR = (255, 100, 100)  # Light red
RAIDER_BULLET_LIFETIME = 1.5  # Seconds

# ═════════════════════════════════════════════════════════════════════════
# HAZARD ZONE SETTINGS
# ═════════════════════════════════════════════════════════════════════════
RADIATION_ZONE_DAMAGE_RATE = 20  # Radiation points per second
RADIATION_ZONE_COLOR = (0, 255, 0)  # Green
RADIATION_ZONE_ALPHA = 50  # Transparency

# ═════════════════════════════════════════════════════════════════════════
# GAME BALANCE
# ═════════════════════════════════════════════════════════════════════════
MUTANT_SPAWN_INITIAL_INTERVAL = 5.0  # Seconds between spawns at start
MUTANT_SPAWN_MIN_INTERVAL = 3.0  # Minimum spawn interval (gets harder)
MUTANT_SPAWN_DECREASE_RATE = 0.1  # How much faster spawns get

# ═════════════════════════════════════════════════════════════════════════
# COLORS (for UI and visuals)
# ═════════════════════════════════════════════════════════════════════════
COLOR_BG = (40, 35, 30)  # Background
COLOR_GROUND = (60, 55, 45)  # Ground color
COLOR_UI_TEXT = (255, 255, 255)  # White text
COLOR_UI_HEALTH = (255, 50, 50)  # Red for health
COLOR_UI_RADIATION_LOW = (100, 255, 100)  # Green
COLOR_UI_RADIATION_MED = (255, 200, 0)  # Yellow
COLOR_UI_RADIATION_HIGH = (255, 50, 50)  # Red

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
