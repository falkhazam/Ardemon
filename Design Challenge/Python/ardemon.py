class Ardemon:
    def __init__(self, level):
        self.base_health = 50
        self.base_damage = 10
        self.max_health = self.base_health
        self.max_damage = self.base_damage

        self.attacks = {}
        self.attack_names = []
        self.active_attack = None

        self.level = level           
        self.total_xp = 0
        self.available_xp = 0

        self.accuracy = 50 # percentage chance of attack hitting
        self.last_pet_time = 0
    
    def reset(self):
        self.damage = self.max_damage
        self.health = self.max_health
    
    def recalculate(self):
        self.max_damage = self.base_damage * (self.level + 1)
        self.max_health = self.base_health * (self.level + 1)

        self.reset()
    
    def upgrade_amount(self):
        return 200 + 20*(self.level-1)

    def level_up(self):
        while (self.upgrade_amount() <= self.available_xp):
            self.available_xp -= self.upgrade_amount()
            self.level += 1
    
        self.recalculate()
    
    def add_xp(self, steps):
        xp = steps
        self.total_xp += xp
        self.available_xp += xp
    
    def __repr__(self):
        return f"Lv.{self.level} {self.__class__.__name__},HP: {self.health}"
    
    def __str__(self):
        return f"{self.__class__.__name__},Lv.{self.level} {self.available_xp}/{self.upgrade_amount()}"
    
    def pet(self):
        self.accuracy += (100-self.accuracy)*0.02
    
    def attack(self, enemy, name):
        pass

    def toggle_attack(self):
        self.attack_names = self.attack_names[1:] + [self.attack_names[0]]
        self.active_attack = self.attack_names[0]


class LavaType(Ardemon):
    def __init__(self, level):
        super().__init__(level)

        self.base_damage = round(self.base_damage*1.5) # does slightly more damage than usual

        self.recalculate()
    
    def add_xp(self, steps): # fire type levels up slightly faster than normal
        xp = steps*(self.level + 1)
        self.total_xp += xp
        self.available_xp += xp


class OceanType(Ardemon):
    def __init__(self, level):
        super().__init__(level)
        
        self.recalculate()
        
    def add_xp(self, steps): # ocean type levels up significantly faster
        xp = steps*(self.level + 3)
        self.total_xp += xp
        self.available_xp += xp
    
    def reset(self):
        self.damage = self.max_damage
        self.health = self.max_health
    
    
class TreeType(Ardemon):
    def __init__(self, level):
        super().__init__(level)

        self.base_damage = round(self.base_damage*0.5) # inflicts lower damage
        self.base_health *= 3 # tree type has more hp

        self.recalculate()


class LightningType(Ardemon):
    def __init__(self, level):
        super().__init__(level)

        self.base_damage *= 3 # lightning type does significantly more damage
        self.base_health = round(self.base_health*0.5) # has significantly less health as well
        
        self.recalculate()
