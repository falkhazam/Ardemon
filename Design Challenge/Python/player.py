from creatures import *
from ECE16Lib.Communication import Communication
from ECE16Lib.Pedometer import Pedometer

# Pedometer values
fs = 50  # sampling rate
num_samples = 250  # 5 seconds of data @ 50Hz

class Player:
    def __init__(self, port, ardemon=[]):
        self.port = port
        self.ardemon = ardemon

        self.comms = Communication(self.port, 115200)
        self.comms.clear()                   # just in case any junk is in the pipes
        self.comms.send_message("wearable")  # begin sending data

        self.total_steps = 0
        self.active_steps = 0

        self.battling = False
        
        if len(self.ardemon) > 0:
            self.active_ardemon = self.ardemon[0]
        else:
            self.active_ardemon = None
        
        self.pedometer = Pedometer(num_samples, fs, [])

        self.selecting = False
        self.spawn = False
        self.challenge = False
        self.challenge_time = 0
        self.incoming = False
    
    def switch_ardemon(self):
        if len(self.ardemon) > 1:
            self.ardemon = self.ardemon[1:] + [self.ardemon[0]]
            self.active_ardemon = self.ardemon[0]
        
        species = None
        if isinstance(self.active_ardemon, LavaType):
            species = "LAVA"
        elif isinstance(self.active_ardemon, OceanType):
            species = "OCEAN"
        elif isinstance(self.active_ardemon, TreeType):
            species = "TREE"
        elif isinstance(self.active_ardemon, LightningType):
            species = "LIGHTNING"
        
        self.write(species)
    
    def change_attack(self):
        self.active_ardemon.toggle_attack()
    
    def convert_xp(self):
        if self.active_ardemon:
            self.active_ardemon.add_xp(self.active_steps)
            self.active_steps = 0
    
    def add_steps(self, steps):
        self.active_steps += steps - self.total_steps
        self.total_steps = steps
        
        self.convert_xp()

    def level_up(self):
        if self.active_ardemon:
            self.active_ardemon.level_up()

    def pet(self, t, delay):
        if self.active_ardemon:
            if (t - self.active_ardemon.last_pet_time > delay):
                self.active_ardemon.pet()
                self.active_ardemon.last_pet_time = t
                return True
        return False
    
    def write(self, string):
        self.comms.send_message(string)

    def receive(self):
        return self.comms.receive_message()

        



    



