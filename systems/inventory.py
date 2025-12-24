from enums import ItemType, WeaponType


class Item:
    def __init__(self, name, item_type, description="", weight=1):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.weight = weight
        self.stackable = False
        self.stack_size = 1
        self.max_stack = 99


class Weapon(Item):
    def __init__(self, name, weapon_type, damage, fire_rate, ammo_type, durability):
        super().__init__(name, ItemType.WEAPON, weight=5)
        self.weapon_type = weapon_type
        self.damage = damage
        self.fire_rate = fire_rate
        self.ammo_type = ammo_type
        self.durability = durability
        self.max_durability = durability
        self.ammo_in_mag = 0
        self.mag_size = 10


class Consumable(Item):
    def __init__(self, name, health_restore=0, hunger_restore=0,
                 thirst_restore=0, rad_restore=0):
        super().__init__(name, ItemType.CONSUMABLE, weight=0.5)
        self.health_restore = health_restore
        self.hunger_restore = hunger_restore
        self.thirst_restore = thirst_restore
        self.rad_restore = rad_restore
        self.stackable = True
        self.max_stack = 10

    def use(self, player):
        player.heal(self.health_restore)
        player.eat(self.hunger_restore)
        player.drink(self.thirst_restore)
        if self.rad_restore > 0:
            player.use_rad_away(self.rad_restore)


class Equipment(Item):
    def __init__(self, name, equipment_type, protection_value):
        super().__init__(name, ItemType.EQUIPMENT, weight=3)
        self.equipment_type = equipment_type
        self.protection_value = protection_value
        self.durability = 100


class Material(Item):
    def __init__(self, name, description=""):
        super().__init__(name, ItemType.MATERIAL, weight=0.2)
        self.stackable = True
        self.max_stack = 50
        self.description = description


class Inventory:
    def __init__(self, max_weight=50):
        self.max_weight = max_weight
        self.current_weight = 0
        self.items = []

    def add_item(self, item):
        if self.current_weight + item.weight > self.max_weight:
            return False

        if item.stackable:
            for inv_item in self.items:
                if (inv_item.name == item.name and
                        inv_item.stack_size < inv_item.max_stack):
                    inv_item.stack_size += 1
                    self.current_weight += item.weight
                    return True

        self.items.append(item)
        self.current_weight += item.weight
        return True

    def remove_item(self, item):
        if item in self.items:
            self.current_weight -= item.weight * item.stack_size
            self.items.remove(item)
            return True
        return False