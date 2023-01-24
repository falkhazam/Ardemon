from ardemon import *

class Ardizard(LavaType):
    def __init__(self, level):
        super().__init__(level)

        self.attacks = {
            "Flamethrower": f"Deal {self.damage} dmg,+25% vs Tree,0 vs Ocean",
            "Fireball": f"Deal {self.damage*2} dmg,+25% vs Tree,Take {round(self.damage*0.75)} dmg",
            "Evaporate": f"Deal {self.damage*0.75} dmg,+30% vs Ocean,0 vs Lightning"
        }

        self.attack_names = ["Flamethrower", "Fireball", "Evaporate"]

        self.active_attack = self.attack_names[0]
        
        
    def attack(self, enemy, name):
        dmg = 0
        if name == "Flamethrower":
            if isinstance(enemy, TreeType):
                dmg = round(self.damage*1.25)
                enemy.health -= dmg
            
            elif isinstance(enemy, OceanType):
                pass

            else:
                dmg = self.damage*1.25
                enemy.health -= dmg
        
        elif name == "Fireball":
            if isinstance(enemy, TreeType):
                dmg = round(self.damage*2*1.25)
                enemy.health -= dmg

            else:
                dmg = self.damage*2
                enemy.health -= dmg
            
            self.health -= round(self.damage*0.75)
    
        elif name == "Evaporate":
            if isinstance(enemy, OceanType):
                dmg = round(self.damage*0.75*1.3)
                enemy.health -= dmg

            elif isinstance(enemy, LightningType):
                pass

            else:
                dmg = round(self.damage*0.75)
                enemy.health -= dmg
        
        return f"Dealt {dmg} dmg!"

class Ardtoise(OceanType):
    def __init__(self, level):
        super().__init__(level)

        self.attacks = {
            "Whirlpool": f"Deal {self.damage} dmg,+25% vs Lava,0 vs Lightning",
            "Tidal Wave": f"Deal {self.damage*0.75} dmg,+50% vs Lava,",
            "Dive": f"Heal {round(self.max_health/4)}HP,(up to max),"
        }

        self.attack_names = ["Whirlpool", "Tidal Wave", "Dive"]

        self.active_attack = self.attack_names[0]

    def attack(self, enemy, name):
        dmg = 0
        if name == "Whirlpool":
            if isinstance(enemy, LavaType):
                dmg = round(self.damage*1.25)
                enemy.health -= dmg
                
            if isinstance(enemy, LightningType):
                pass

            else:
                dmg = self.damage
                enemy.health -= dmg
        elif name == "Tidal Wave":
            if isinstance(enemy, LavaType):
                dmg = round(self.damage*1.5*0.75)
                enemy.health -= dmg
            else:
                dmg = round(self.damage*0.75)
                enemy.health -= dmg
        elif name == "Dive":
            self.health += round(self.max_health/4)
            if self.health > self.max_health:
                self.health = self.max_health
            return f"Healed to {self.health}HP!"
        
        return f"Dealt {dmg} dmg!"
    

class Ardusaur(TreeType):
    def __init__(self, level):
        super().__init__(level)

        self.attacks = {
            "LeafBlade": f"Deal {round(self.damage*1.25)} dmg,-30% vs Lava,",
            "Gigadrain": f"Steal {round(self.damage*0.7)} HP,0 vs Lava,",
            "Overgrowth": f"Increase dmg by,+{round(self.damage*0.9)},{self.damage}->{self.damage+round(self.damage*0.9)}"
        }

        self.attack_names = ["LeafBlade", "Gigadrain", "Overgrowth"]

        self.active_attack = self.attack_names[0]

    def attack(self, enemy, name):
        dmg = 0
        if name == "LeafBlade":
            if isinstance(enemy, LavaType):
                dmg = round(self.damage*1.25*0.7)
                enemy.health -= dmg
            else:
                dmg = round(self.damage*1.25)
                enemy.health -= dmg
        elif name == "Gigadrain":
            if not isinstance(enemy, LavaType):
                enemy.health -= round(self.damage*0.7)
                self.health += round(self.damage*0.7)
                return f"Stole {round(self.damage*0.7)}HP!"
        elif name == "Overgrowth":
            self.damage += round(self.damage*0.9)
            self.attacks = {
                "LeafBlade": f"Deal {round(self.damage*1.25)} dmg,-30% vs Lava,",
                "Gigadrain": f"Steal {round(self.damage*0.7)} HP,0 vs Lava,",
                "Overgrowth": f"Increase dmg by,+{round(self.damage*0.9)},{self.damage}->{self.damage+round(self.damage*0.9)}"
            }
            return f"Buffed DMG->{self.damage}"
        return f"Dealt {dmg} dmg!"

class Pikardchu(LightningType):
    def __init__(self, level):
        super().__init__(level)

        self.attacks = {
            "Lightning Bolt": f"Deal {self.damage} dmg,-20% vs Ocean,",
            "Short Circuit": f"Deal {self.damage*2} dmg,0 vs Lava,Lower HP by 70%",
            "Induct": f"Heal {round(self.max_health/5)}HP,(up to max),"
        }

        self.attack_names = ["Lightning Bolt", "Short Circuit", "Induct"]

        self.active_attack = self.attack_names[0]

    def attack(self, enemy, name):
        dmg = 0
        if name == "Lightning Bolt":
            if isinstance(enemy, OceanType):
                dmg = round(self.damage*0.8)
                enemy.health -= dmg
            else:
                dmg = self.damage
                enemy.health -= dmg
        elif name == "Short Circuit":
            if not isinstance(enemy, LavaType):
                dmg = self.damage*2
                enemy.health -= dmg
                self.health -= round(self.health*0.7)
        elif name == "Induct":
            self.health += round(self.max_health/3)
            if self.health > self.max_health:
                self.health = self.max_health
            return f"Healed to {self.health}HP!"
        
        return f"Dealt {dmg} dmg!"

class Floartle(OceanType):
    def __init__(self, level):
        super().__init__(level)

        self.attacks = {
            "Bubbool": f"Deal {self.damage} dmg,+20% vs Lava,0 vs Tree",
            "High Tide": f"Deal {round(self.damage*1.25)} dmg,+50% vs Lava,Lower HP by 20%",
            "Shower": f"Heal {round(self.max_health/4)}HP,(up to max),"
        }

        self.attack_names = ["Bubbool", "High Tide", "Dive"]

        self.active_attack = self.attack_names[0]

    def attack(self, enemy, name):
        dmg = 0
        if name == "Bubbool":
            if isinstance(enemy, LavaType):
                dmg = round(self.damage*1.2)
                enemy.health -= dmg
                
            if isinstance(enemy, TreeType):
                pass

            else:
                dmg = self.damage
                enemy.health -= dmg
        elif name == "High Tide":
            if isinstance(enemy, LavaType):
                dmg = round(self.damage*1.5*1.25)
                enemy.health -= dmg
            else:
                dmg = round(self.damage*1.25)
                enemy.health -= dmg
            self.health -= round(self.health*0.2)
        elif name == "Shower":
            self.health += round(self.max_health/4)
            if self.health > self.max_health:
                self.health = self.max_health
            return f"Healed to {self.health}HP!"
        
        return f"Dealt {dmg} dmg!"


class MISSINGNO(LightningType):
    def __init__(self, level):
        super().__init__(level)

        self.attacks = {
            "Insulator": f"Deal {self.damage*2} dmg, 0 vs Tree, +100% vs Lightning",
            "Magma": f"Deal {self.damage*2} dmg,0 vs Lava,+100% vs Tree",
            "Lake": f"Deal {self.damage*2} dmg,0 vs Ocean, +100% vs Lava"
        }

        self.attack_names = ["Thunder", "Magma", "Lake"]

        self.active_attack = self.attack_names[0]

    def attack(self, enemy, name):
        dmg = 0
        if name == "Insulator":
            if isinstance(enemy, LightningType):
                dmg = round(self.damage*2)
                enemy.health -= dmg
            elif isinstance(enemy, TreeType):
                pass
            else:
                dmg = self.damage
                enemy.health -= dmg
            
        if name == "Magma":
            if isinstance(enemy, TreeType):
                dmg = round(self.damage*2)
                enemy.health -= dmg
            elif isinstance(enemy, LavaType):
                pass
            else:
                dmg = self.damage
                enemy.health -= dmg

        if name == "Lake":
            if isinstance(enemy, LavaType):
                dmg = round(self.damage*2)
                enemy.health -= dmg
            elif isinstance(enemy, OceanType):
                pass
            else:
                dmg = self.damage
                enemy.health -= dmg
        
        return f"Dealt {dmg} dmg!"



class Intmander(LavaType):
    def __init__(self, level):
        super().__init__(level)

        self.attacks = {
            "Ember ": f"Deal {self.damage} dmg,-20% vs Ocean,",
            "Firetail": f"Deal {round(self.damage*1.5)} dmg,0 vs Ocean,Lower HP by 10%",
            "Sauna": f"Heal {round(self.max_health/3)}HP,(up to max),"
        }

        self.attack_names = ["Ember", "Firetail", "Sauna"]

        self.active_attack = self.attack_names[0]

    def attack(self, enemy, name):
        dmg = 0
        if name == "Ember":
            if isinstance(enemy, OceanType):
                dmg = round(self.damage*0.8)
                enemy.health -= dmg
            else:
                dmg = self.damage
                enemy.health -= dmg
        elif name == "Firetail":
            if not isinstance(enemy, OceanType):
                dmg = round(self.damage*1.5)
                enemy.health -= dmg
                self.health -= round(self.health*0.1)
        elif name == "Sauna":
            self.health += round(self.max_health/3)
            if self.health > self.max_health:
                self.health = self.max_health
            return f"Healed to {self.health}HP!"
        
        return f"Dealt {dmg} dmg!"

class Boolbasaur(TreeType):
    def __init__(self, level):
        super().__init__(level)

        self.attacks = {
            "Papercut": f"Deal {round(self.damage*1.25)} dmg,-30% vs Lava,",
            "Sunlight": f"Steal {round(self.damage*0.7)} HP,0 vs Lava,",
            "Go Green!": f"Heal {round(self.max_health/3)}HP,(up to max),"
        }

        self.attack_names = ["Papercut", "Sunlight", "Go Green!"]

        self.active_attack = self.attack_names[0]

    def attack(self, enemy, name):
        dmg = 0
        if name == "Papercut":
            if isinstance(enemy, LavaType):
                dmg = round(self.damage*1.25*0.3)
                enemy.health -= dmg
            else:
                dmg = round(self.damage*1.25)
                enemy.health -= dmg
        elif name == "Sunlight":
            if not isinstance(enemy, LavaType):
                enemy.health -= round(self.damage*0.7)
                self.health += round(self.damage*0.7)
                return f"Stole {round(self.damage*0.7)}HP!"
        elif name == "Go Green!":
            self.health += round(self.max_health/3)
            if self.health > self.max_health:
                self.health = self.max_health
            return f"Healed to {self.health}HP!"
        return f"Dealt {dmg} dmg!"


def doctests(): # sanity checks
    """
    >>> pikachu = Pikardchu(3)
    >>> pikachu.level
    3
    >>> pikachu.damage
    120
    >>> pikachu.health
    100
    >>> ardtoise = Ardtoise(2)
    >>> ardtoise.health
    150
    >>> ardtoise
    Lv.2 Ardtoise,HP: 150
    >>> pikachu.attack(ardtoise, "Lightning Bolt")
    'Dealt 96 dmg!'
    >>> ardtoise.health
    54
    >>> ardusaur = Ardusaur(4)
    >>> ardusaur.health
    750
    >>> pikachu.attack(ardusaur, "Short Circuit")
    'Dealt 240 dmg!'
    >>> ardusaur.health
    510
    >>> pikachu.health
    30
    >>> pikachu.attack(ardusaur, "Induct")
    'Healed to 63HP!'
    >>> pikachu.health
    63
    >>> ardusaur.attack(pikachu, "LeafBlade")
    'Dealt 31 dmg!'
    >>> pikachu.health
    32
    >>> ardusaur.attack(pikachu, "Gigadrain")
    'Stole 18HP!'
    >>> ardusaur.health
    528
    >>> pikachu.health
    14
    >>> ardusaur.attack(pikachu, "Overgrowth")
    'Buffed DMG->47'
    >>> ardusaur.damage
    47
    >>> ardusaur.reset()
    >>> ardusaur.health
    750
    >>> ardusaur.damage
    25
    >>> ardtoise.attack(ardusaur, "Whirlpool")
    'Dealt 30 dmg!'
    >>> ardusaur.health
    720
    >>> ardtoise.attack(ardusaur, "Tidal Wave")
    'Dealt 22 dmg!'
    >>> ardusaur.health
    698
    >>> ardtoise.attack(ardusaur, "Dive")
    'Healed to 92HP!'
    >>> ardtoise.health
    92
    >>> char = Ardizard(3)
    >>> char.attack(ardtoise, "Flamethrower")
    'Dealt 0 dmg!'
    >>> ardtoise.health
    92
    >>> char.attack(ardusaur, "Flamethrower")
    'Dealt 75 dmg!'
    >>> ardusaur.health
    623
    >>> char.health
    200
    >>> char.attack(ardusaur, "Fireball")
    'Dealt 150 dmg!'
    >>> char.health
    155
    >>> ardusaur.health
    473
    >>> char.attack(ardtoise, "Evaporate")
    'Dealt 58 dmg!'
    >>> ardtoise.health
    34
    >>> char.attack(pikachu, "Evaporate")
    'Dealt 0 dmg!'
    >>> pikachu.health
    14
    >>> pikachu.upgrade_amount()
    240
    >>> pikachu.available_xp += 510
    >>> pikachu.level_up()
    >>> pikachu.level
    5
    >>> pikachu.available_xp
    10
    >>> pikachu.level_up()
    >>> pikachu.level
    5
    >>> pikachu.available_xp
    10
    >>> pikachu.damage
    180
    >>> pikachu.health
    150
    >>> intmander = Intmander(3)
    >>> intmander.attack(ardtoise, "Firetail")
    'Dealt 0 dmg!'
    >>> intmander.attack(ardusaur, "Firetail")
    'Dealt 90 dmg!'
    >>> intmander.attack(ardtoise, "Ember")
    'Dealt 48 dmg!'
    >>> intmander.attack(pikachu, "Firetail")
    'Dealt 90 dmg!'
    >>> missingno = MISSINGNO(8)
    >>> missingno.attack(pikachu, "Insulator")
    'Dealt 540 dmg!'
    >>> missingno.attack(ardusaur, "Insulator")
    'Dealt 0 dmg!'
    >>> missingno.attack(intmander, "Insulator")
    'Dealt 270 dmg!'
    >>> missingno.attack(ardusaur, "Magma")
    'Dealt 540 dmg!'
    >>> missingno.attack(intmander, "Magma")
    'Dealt 0 dmg!'
    >>> missingno.attack(pikachu, "Magma")
    'Dealt 270 dmg!'
    >>> missingno.attack(intmander, "Lake")
    'Dealt 540 dmg!'
    >>> missingno.attack(ardtoise, "Lake")
    'Dealt 0 dmg!'
    >>> missingno.attack(pikachu, "Lake")
    'Dealt 270 dmg!'

    """
