from creatures import *
from player import *
from datetime import datetime
import pytz
import time

tz = pytz.timezone('America/Los_Angeles')

class Display:
    def __init__(self, player):
        self.player = player
    
    def update(self):
        if self.player.active_ardemon:
            self.player.write(f"Steps: {self.player.total_steps},{datetime.now(tz).strftime('%m/%d %H:%M')},{self.player.active_ardemon.__str__()}OLED")
        else:
            self.player.write(f"Steps: {self.player.total_steps},{datetime.now(tz).strftime('%m/%d %H:%M')},No Ardemon,OLED")
    
    def select_ardemon(self, selected=False):
        if selected:
            self.player.write(f"Selected:,{self.player.active_ardemon.__repr__()},OLED")
        else:
            self.player.write(f"Select?,{self.player.active_ardemon.__str__()},DMG:{self.player.active_ardemon.max_damage} HP:{self.player.active_ardemon.max_health}OLED")
    
    def select_attack(self, selected=False):
        attack = self.player.active_ardemon.active_attack
        if selected:
            self.player.write(f"Selected Attack:,{attack},,OLED")
        else:
            self.player.write(f"{attack},{self.player.active_ardemon.attacks[attack]}OLED")

    def attack(self, enemy, message):
        if message != "Missed!":
            self.player.write("BUZZ")
        self.player.write(f"HP:{self.player.active_ardemon.health},Enemy HP:{enemy.health},{message},OLED")
    
    def level_up(self):
        self.player.write(f"Leveled up!,{self.player.active_ardemon.__class__.__name__}->{self.player.active_ardemon.level},\
HP->{self.player.active_ardemon.max_health},DMG->{self.player.active_ardemon.max_damage}OLED")
        self.player.write("BUZZ")
    
    def ready_screen(self, enemy):
        self.player.write(f"FIGHT!,Lv.{self.player.active_ardemon.level} {self.player.active_ardemon.__class__.__name__},VS,\
{enemy.level} {enemy.__class__.__name__}OLED")
    
    def turn_screen(self, enemy, move):
        species = None
        if isinstance(enemy, LavaType):
            species = "Lava"
        elif isinstance(enemy, OceanType):
            species = "Ocean"
        elif isinstance(enemy, TreeType):
            species = "Tree"
        elif isinstance(enemy, LightningType):
            species = "Lightning"
        
        if move:
            self.player.write(f"Your Move!,HP:{self.player.active_ardemon.health},Enemy HP:{enemy.health},Type:{species}OLED")
        else:
            self.player.write(f"Waiting...!,HP:{self.player.active_ardemon.health},Enemy HP:{enemy.health},Type:{species}OLED")
    
    def loss(self, xp):
        self.player.write(f"Defeat!,Lost {xp}XP,{self.player.active_ardemon.__str__()}OLED")
        self.player.write("BUZZ")
    
    def win(self, xp):
        self.player.write(f"Victory!,Won {xp}XP,{self.player.active_ardemon.__str__()}OLED")
        self.player.write("BUZZ")
    
    def draw(self):
        self.player.write(f"Draw!,No XP Change,{self.player.active_ardemon.__str__()}OLED")
        self.player.write("BUZZ")
    
    def pet(self, successful, delay):
        if successful:
            self.player.write(f"Lv.{self.player.active_ardemon.level} {self.player.active_ardemon.__class__.__name__},Friendship++ !,\
New->{self.player.active_ardemon.accuracy}OLED")
        else:
            self.player.write(f"Lv.{self.player.active_ardemon.level} {self.player.active_ardemon.__class__.__name__},Unable to pet,Time remaining:,\
{round((delay-time.time() + self.player.active_ardemon.last_pet_time)/60)}minsOLED")

    def searching(self):
        self.player.write("Searching for,battle...,,OLED")
    
    def time_out(self):
        self.player.write("Unable to find,battle,,OLED")
    
    def offer(self, choice):
        self.player.write(f"Lv.{choice.level} {choice.__class__.__name__},Appeared!,Button: Catch,PhotoR: IgnoreOLED")
    
    def accept(self, choice):
        self.player.write(f"Lv.{choice.level} {choice.__class__.__name__},Added to,Inventory!,OLED")
    
    def decline(self, choice):
        self.player.write(f"Lv.{choice.level} {choice.__class__.__name__},Ignored.,,OLED")
    
    def challenged(self):
        self.player.write(f"Challenge,Incoming!,Button:Accept,PhotoR:DeclineOLED")
    
    def starting(self):
        self.player.write(f"Starting Battle!,,,")





    
    



    



        
